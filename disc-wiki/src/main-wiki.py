# -*- coding: utf-8 -*-
import sys

import numpy as np
import pandas as pd
import psycopg2
import nest_asyncio
nest_asyncio.apply()

from discord.ext import commands
#import discord.app_commands
import discord
from discord.ui import Button, View

import toolbox.cogs as tbcogs




class WikiHelper(commands.HelpCommand):
    def __init__(self):
        super().__init__()
        
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="**🔎 Commandes**", description="*Tapez **w!help <nomdelacommande>** pour avoir plus d'informations sur une en particulier.*")
        for cog in mapping:
            if cog is not None:
                if cog.qualified_name != 'Admin':
                    embed.add_field(name=cog.qualified_name,value=', '.join([command.name for command in mapping[cog]]), inline=False)
        await self.get_destination().send(embed=embed)
            
    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)
    
    async def send_group_help(self, group):
        return await super().send_group_help(group)
    
    async def send_command_help(self, command):
        embed = discord.Embed(title=f"**{command.name}**", description=command.description)
        await self.get_destination().send(embed=embed)

class WikiBot(commands.Bot):
    def __init__(self):
        # All but the THREE privileged ones
        intents = discord.Intents.default()  
        # Subscribe to the Message Content and Members intent
        intents.message_content = True  
        intents.members = True
        super().__init__(command_prefix="n!", intents=intents)
        self.dsn="dbname=gameserv user=postgres password='minnashojo'"

    async def on_ready(self):
        await self.add_cog(tbcogs.GalleryCog(self))
        await self.add_cog(tbcogs.CharacterCog(self))
        await self.add_cog(tbcogs.RpCog(self))
        await self.add_cog(tbcogs.PlayerCog(self))
        await self.add_cog(tbcogs.MusicCog(self))
        await self.add_cog(tbcogs.AdminCog(self))

        self.help_command = WikiHelper()
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="faire maigrir les rageux"))
        print(f"{self.user.display_name} est connecté.")

    async def on_message(self, message):
        await bot.process_commands(message)


bot = WikiBot()
bot.run("DISCORD_KEY_PLACEHOLDER")

# @bot.event
# async def on_member_join(member):
#     players = pd.read_csv('players.csv',header=0,sep=';')
#     player_list = list(players['id'])
#     if member.id in player_list:
#         row = players[players['id'] == member.id].iloc[0]
#         await member.add_roles(discord.utils.get(member.guild.roles, id=int(row['role_id'])))
#     else:
#         print("ok")
#         await member.add_roles(discord.utils.get(member.guild.roles, id=955544439282077736))
        

        
# @bot.command(name='addposttmp')
# async def addposttmp(ctx, *args):
#     print("Commande post")
#     if ctx.author.id == 164786647072899072:
#         await ctx.send(args[0])
