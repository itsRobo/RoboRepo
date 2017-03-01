import discord
from discord.ext import commands
import random
#from discord.ext import commands

class pickorder:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def pickorder(self, ctx, message):
 
		messageWithoutCall = ctx.message.content.replace("!pickorder", "")
		id = messageWithoutCall.split( )

		num=1
		numbers=[];

		for name in id: 
#			await self.bot.say( str(num) + ". " + name) this felt uneccesary
			numbers.append(num)
			num+=1

		random.shuffle(id) #picks a random order for the names

		for num2 in numbers: 
			await self.bot.say( str(num2) + ". " + id[num2])

def setup(bot):
	bot.add_cog(pickorder(bot))