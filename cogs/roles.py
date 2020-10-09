
import discord
import discord.guild
from discord.ext import commands
import discord.member
import json

config = json.load(open("config.json"))


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    guild_id = [750959329464549466, 763041558014066699]
    @commands.command()
    async def hire(self, ctx, member : discord.Member):
        if member == None:
            return await ctx.send("run this command again but next time actually mention someone to hire")
        for guild_id in config["servers"]:
            guild = self.bot.get_guild(guild_id)
            role = discord.utils.get(guild.roles, name="members")
            member = guild.get_member(member.id)
            try:
                await member.add_roles(role)
                await ctx.send(f"Added {role} role to {member.mention} in {guild}")
            except:
                await ctx.send("A error occured while removing the roles")


    @commands.command()
    async def fire(self, ctx, member : discord.Member):
        if member == None:
            return await ctx.send("run this command again but next time actually mention someone to fire")
        for guild_id in config["servers"]:
            guild = self.bot.get_guild(guild_id)
            role = discord.utils.get(guild.roles, name="members")
            member = guild.get_member(member.id)
            try:
                await member.remove_roles(role)
                await ctx.send(f"fired {member.mention} and removed him as a {role}")    
            except:
                await ctx.send("A error occured while adding the roles")
    




        

def setup(bot):               
    bot.add_cog(Roles(bot))
