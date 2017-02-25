import discord
from discord.ext import commands

try: # check if BeautifulSoup4 is installed
	from bs4 import BeautifulSoup
	soupAvailable = True
except:
	soupAvailable = False
import aiohttp

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

    @commands.command(pass_context=True)
    async def echo(self, ctx, message):

        author = ctx.message.author
        myString = ctx.message.content
        await self.bot.say("{} {}".format(author.mention, myString[6:]))

    @commands.command()
    async def rlnow(self):
        """How many players are online atm?"""

        #Your code will go here
        url = "https://steamdb.info/app/252950/graphs/" #build the web adress
        async with aiohttp.get(url) as response:
            soupObject = BeautifulSoup(await response.text(), "html.parser")
        try:
            online = soupObject.find(class_='home-stats').find('li').find('strong').get_text()
            await self.bot.say(online + ' players are playing Rocket League at the moment')
        except:
           await self.bot.say("Couldn't load amount of players. No one is playing this game anymore or there's an error.")


def setup(bot):
	if soupAvailable:
		bot.add_cog(Mycog(bot))
	else:
		raise RuntimeError("You need to run `pip3 install beautifulsoup4`")