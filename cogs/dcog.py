import discord
from discord.ext import commands
import os
#from discord.ext import commands

class dcog:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def linkmmr(self, ctx, message, member: discord.Member):

		triggerSubtext = "/id/" #this is the string directly before the id in the url
		id = message

		if( "http://steamcommunity.com/id" in message ):
			id = id[id.find(triggerSubtext)+len(triggerSubtext):]

		#if os.path.isfile("data/mmr/mmr.txt"):
		file = open( "data/mmr/mmr.txt", a)
		file.write( discord.member + "linksto" + id)
		await self.bot.say("Success!")
		#else:
			await self.bot.say("Something went wrong!")

def setup(bot):
	bot.add_cog(dcog(bot))