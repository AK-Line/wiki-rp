from discord.ext import commands
import discord
from discord.ui import Button, View
import copy as cp

BUT_GRN, BUT_RED, BUT_BLU, BUT_GRA = discord.ButtonStyle.green, discord.ButtonStyle.red, discord.ButtonStyle.blurple, discord.ButtonStyle.gray

class ValidationButton(Button):
    """
    The view using at least one of these Buttons must implement the
    validate() method.
    """
    def __init__(self, row, label="Valider", custom_id="val"):
        super().__init__(label=label,row=row,style=BUT_BLU,custom_id=custom_id)
    
    async def callback(self, interaction):
        """
        Only calls the validate function of the View
        """
        await self.view.validate(interaction, self)

class IncrementButton(Button):
    """
    The view using at least one of these Buttons must implement the
    increment() method.
    """
    def __init__(self, row, increment_value, label=None, custom_id=None):
        self.increment_value = increment_value
        if label is None:
            label = str(self.increment_value)
            if self.increment_value > 0:
                self.label = f"+{increment_value}"
        self.custom_id = custom_id
        if custom_id is None:
            self.custom_id = self.label
        super().__init__(label=label,row=row,style=BUT_BLU,custom_id=custom_id)
    
    async def callback(self, interaction):
        """
        Only calls the increment function of the View
        """
        await self.view.increment(interaction, self)

class SwitchLightButton(Button):
    """
    The view using at least one of these Buttons must implement the
    switch_light() method.
    """
    def __init__(self, row, label, custom_id=None, status=False):
        super().__init__(label=label,row=row,style=BUT_RED,custom_id=custom_id, emoji="☒")
        self.status = status
        if self.status:
            self.ui_switch()
    
    def ui_switch(self):
        if self.status:
            self.style = BUT_GRN
            self.emoji = "🗹"
        else:
            self.style = BUT_RED
            self.emoji = "☒"

    async def callback(self, interaction):
        """
        Only calls the validate function of the View
        """
        self.status = not self.status
        self.ui_switch()
        await self.view.switch_light(interaction, self)

class SwitchOptionButton(Button):
    """
    The view using at least one of these Buttons must implement the
    switch_option() method.

    option_list should be a list object containing dict with :
    - mandatory key "label"
    - optional key "emoji"
    """
    def __init__(self, row, option_list, custom_id="sob", status=0):
        self.status = status
        self.option_list = option_list
        current_option = self.option_list[self.status]
        super().__init__(label=current_option["label"],row=row,style=BUT_BLU,custom_id=custom_id, emoji=current_option.get("emoji", None))
        self.status = status
    
    def ui_switch(self):
        current_option = self.option_list[self.status]
        self.label = current_option["label"]
        self.emoji = current_option.get("emoji", None)

    async def callback(self, interaction):
        """
        Only calls the validate function of the View
        """
        self.status += 1
        if self.status == len(self.option_list):
            self.status = 0
        self.ui_switch()
        await self.view.switch_option(interaction, self)