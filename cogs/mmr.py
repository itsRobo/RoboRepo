import discord
from discord.ext import commands
import os
#from discord.ext import commands

class mmr:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def linkmmr(self, ctx, steamID, user : discord.User):

		triggerSubtext = "/id/" #this is the string directly before the id in the url
		discordID = user.id

		if( "http://steamcommunity.com/id" in steamID ):
			steamID = steamID[steamID.find(triggerSubtext)+len(triggerSubtext):]

		if os.path.isfile("data/mmr/mmr.txt"):
			file = open( "data/mmr/mmr.txt", "a")
			file.write( str( discordID ) + " " + str(steamID) + "\n")
			await self.bot.say("Success!")
		else:
			await self.bot.say("Something went wrong!")

def setup(bot):
	bot.add_cog(mmr(bot))