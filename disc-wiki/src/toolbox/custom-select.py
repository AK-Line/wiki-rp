from discord.ext import commands
import discord
from discord.ui import Select, View
import copy as cp

class MultiSelect(Select):
    """
    Multi-usage Selector for the Wiki
    Possible type values : (rp,player,illu_type,oc,filter,filteroptions)

    Internal values :
    self.item_list : dict of options. Keys of the dict needs to be the 
    "internal" values -> positive ints. values are the labels associated
    self.page : current page
    self.max_page : maximum possible page. If options > 20, it will be
    different from 0.
    self.options_full : complete list of options as SelectOption items
    self.selected : list of selected options (crazy)   
    self.options : local options (page level)
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

        super().__init__(placeholder=placeholder,min_values=1,max_values=self.max_values,options=self.options,row=row,custom_id=custom_id)
    
    def item_load(item_list):
        """
        Creates the full list of options and initialize the first page.
        Can be reused if the list changes.

        """
        self.item_list = item_list
        self.page = 0
        self.max_page = (len(self.item_list)-1)//20
        self.options_full = [discord.SelectOption(label=item_list[k],value=k) for k in self.item_list.keys()]
        self.selected = []
        self.options = self.options_generator()

    def options_generator(self):
        """
        Gives a list of options based on current page.
        """
        if max_page = 0:
            return self.options_full
        page_options = []
        if self.page > 0:
            page_options.append(discord.SelectOption(label=f"<--- Page {self.page}"), value=-2)
        page_options += options_full[20*self.page:min(len(self.options),20*self.page+1)]
        if self.page < max_page:
            page_options.append(discord.SelectOption(label=f"Page {self.page} --->"), value=-1)
        return page_options

    def manage_selections(self, new: list):
        """
        Adapts the selection list to the new given elements.
        1- Deletes all the already present elements in the selected list
        2- erases in a FIFO fashion elements of the list if the resulting one is too long for max_values
        option.
        """
        if self.max_values == 1:
            self.selected = [new[0]]
        else:
            new = self.selected + new
            self.selected = []
            [self.selected(x) for x in new if x not in self.selected]
            self.selected = self.selected[-max_values:] 

    async def callback(self, interaction):
        """
        Edit itself if page changes ; update selection list
        
        """
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