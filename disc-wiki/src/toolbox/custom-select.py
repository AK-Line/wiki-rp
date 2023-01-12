from discord.ext import commands
import discord
from discord.ui import Select, View
import copy as cp


    

class MultiSelect(Select):
    """
    Selecteur Multi-usage pour le Wiki

    Possibles valeurs de type : (rp,player,illu_type,oc,filter,filteroptions)
    """
    def __init__(
        self,
        view: discord.View,
        item_list: dict,
        row: int,
        max_values=1: int,
        placeholder="Choix de ...": str,
        custom_id="sel": str,
        type="rp": str,
        disabled=False: bool,
        ):
        self.view = view
        self.max_values = max_values
        self.item_load(item_list)

        super().__init__(placeholder=placeholder,min_values=1,max_values=self.max_values,options=self.options_generator(),row=row,custom_id=custom_id)
    
    def item_load(item_list):
        self.item_list = item_list
        self.page = 0
        self.max_page = (len(self.item_list)-1)//20
        self.options_full = [discord.SelectOption(label=item_list[k],value=k) for k in self.item_list.keys()]
        self.selected = []
        self.options = self.options_generator()

    def options_generator(self):
        if max_page = 0:
            return self.options_full
        page_options = []
        if self.page > 0:
            page_options.append(discord.SelectOption(label=f"<--- Page {self.page}"), value=-2)
        page_options += page_options[20*self.page:min(len(self.options),20*self.page+1)]
        if self.page < max_page:
            page_options.append(discord.SelectOption(label=f"Page {self.page} --->"), value=-1)
        return page_options

    def manage_selections(self, new: list):
        if self.max_values == 1:
            self.selected = [new[0]]
        if self.
 
    async def callback(self, interaction):
        page_change = 0
        current_sel = cp.copy(self.values)
        if -1 in current_sel:
            page_change += 1
            current_sel.remove(-1)
        if -2 in current_sel:
            page_change -= 1
            current_sel.remove(-2)
        self.selected = manage_selections(current_sel)
        if page_change != 0:
            self.page += page_change
            self.options = self.options_generator()
        await self.view.select_edit(interaction,self)