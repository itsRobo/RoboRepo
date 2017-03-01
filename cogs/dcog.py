import discord
from discord.ext import commands
import os
#from discord.ext import commands

class dcog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def linkmmr(self, ctx, steamID, user : discord.User):

		triggerSubtext = "/id/" #this is the string directly before the id in the url
		discordID = user.id
		await self.bot.say("Your ID: " + str(discordID) )

		if( "http://steamcommunity.com/id" in steamID ):
			steamID = steamID[steamID.find(triggerSubtext)+len(triggerSubtext):]

		if os.path.isfile("data/mmr/mmr.txt"):
			file = open( "data/mmr/mmr.txt", "a")
			file.write( str( discordID ) + "linksto " + str(steamID) + "\n")
			await self.bot.say("Success!")
		else:
			await self.bot.say("Something went wrong!")

def setup(bot):
	bot.add_cog(dcog(bot))