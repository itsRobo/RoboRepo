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

		i=1
		numbers=[];

		for name in id: 
			await self.bot.say(i + ". " + name)
			numbers.append(i)
			i+=1

		random.shuffle(id)

		for num in numbers: 
			await self.bot.say(i + ". " + name)
			numbers.append(i)

	def setup(bot):
		bot.add_cog(pickorder(bot))