import discord
from discord.ext import commands
import os
#from discord.ext import commands

class dcog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def linkmmr(self, ctx, steamID, user):

		triggerSubtext = "/id/" #this is the string directly before the id in the url
		steamid = steamID

		if( "http://steamcommunity.com/id" in steamID ):
			steamid = steamid[steamid.find(triggerSubtext)+len(triggerSubtext):]

		if os.path.isfile("data/mmr/mmr.txt"):
			file = open( "data/mmr/mmr.txt", "a")
			file.write( str(user.id) + "linksto " + str(steamid) )
			await self.bot.say("Success!")
		else:
			await self.bot.say("Something went wrong!")

def setup(bot):
	bot.add_cog(dcog(bot))