from discord.ext import commands
import discord
from discord.ui import View
from toolbox.custom-select import *
from toolbox.custom-button import *
import copy as cp
import numpy as np


class OcGalView(View):
    """ #1
        Gallerie d'un OC (tous les arts le concernant)
        (Première page : statistiques)
        Sélecteur RP, Sélecteur joueur, Sélecteur OC (1-1) avec validation
        Boutons : <-5><-1><Auto/Manuel><+1><+5>
    """
    def __init__(self, ctx):
        super().__init__(timeout=180)
        self.ctx = ctx
        self.channel = ctx.channel.id
        self.author = ctx.author.id
        self.oc_df = None #db request with rows at format [oc_id, rp_id, player_id]
        self.rp_dict = None #db request with dict as return value at format {rp_id:rp_name}
        self.player_dict = None #db request with dict as return value at format {player_id:player_name}
        self.rp_filter = None #int type
        self.player_filter = None #int type
        self.oc_filter = None #random selection
        self.current_oc = None 
        self.current_page = 0
        self.nb_page = 0
        
    def setup_buttons(self):
        self.add_item(IncrementButton(row=0, increment_value=-5, label='-5', custom_id="-5"))
        self.add_item(IncrementButton(row=0, increment_value=-1, label='-1', custom_id="-1"))
        self.add_item(ValidationButton(row=0, label="Voir OC", custom_id="switch_oc"))
        self.add_item(IncrementButton(row=0, increment_value=1, label='+1', custom_id="+1"))
        self.add_item(IncrementButton(row=0, increment_value=5, label='+5', custom_id="+5"))
        self.add_item(MultiSelect(view=self, item_list=self.oc_generator(), row=1, max_values=1, placeholder="OC disponibles", custom_id="sel_oc", type="oc", disabled=False))
        self.add_item(MultiSelect(view=self, item_list=self.rp_dict, row=2, max_values=1, placeholder="Filter un RP", custom_id="sel_rp", type="rp", disabled=False))
        self.add_item(MultiSelect(view=self, item_list=self.player_dict, row=3, max_values=1, placeholder="Filtrer un Joueur", custom_id="sel_player", type="player", disabled=False))

    def generate_embed(self):
        pass

    def retrieve_gallery(self):
        pass

    def validate(self, interaction, validate_button):
        pass

    def select_edit(self, interaction, select_button):
        if select_button.custom_id == "sel_oc":
            self.oc_filter = select_button.value[0]
        if select_button.custom_id == "sel_rp":
            self.rp_filter = select_button.value[0]
            [x for x in self.children if x.custom_id=='sel_oc'][0].item_load(self.oc_generator())
        if select_button.custom_id == "sel_player":
            self.player_filter = select_button.value[0]
            [x for x in self.children if x.custom_id=='sel_oc'][0].item_load(self.oc_generator())
        self.generate_embed() #maybe better solution
        #update ui view

    def increment(self, interaction, increment_button):
        self.current_page += increment_button.increment_value
        if self.current_page >= self.nb_page:
            self.current_page -= self.nb_page
        if self.current_page < 0:
            self.current_page += self.nb_page
        self.generate_embed() #maybe not needed
        #update view
        