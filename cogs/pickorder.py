import discord
from discord.ext import commands
import random
#from discord.ext import commands

class pickorder:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def pickorder(self, ctx, message):
 
		id = message.split( )

		num=1
		numbers=[];

		for name in id: 
			await self.bot.say(str(num) + ". " + name)
			numbers.append(i)
			num+=1

		random.shuffle(id) #picks a random order for the names

		for num in numbers: 
			await self.bot.say(i + ". " + name)

def setup(bot):
	bot.add_cog(pickorder(bot))