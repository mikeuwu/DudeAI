import asyncio
import async_cleverbot as ai
import discord
#import discordvc

from gtts import gTTS
from discord.ext import commands

class AI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            if message.content == "dude":
                await message.channel.send(f"Hmm?")
            elif message.content == "dude help":
                await message.channel.send(f"Hmm, I don't have any commands but you can talk with me using dude <message> and i will reply to you & to get info about me use `dude say about you`!")
            elif message.content == "dude say about you":
                await message.channel.send("Hey there, im DudeAI made by mikeuwu#8307, actually im a chatbot you can spend your time with me if you are bored or feeling lonely, you can keep your server active with help of me. If you have any questions/queries or need to give suggestion or need to report a bug please dm mikeuwu#8307")
            else:
                if message.content.startswith("dude "):
                    #if message.author.voice is None:
                    dude = ai.Cleverbot("e/!-F6*FBW'8vZJ8,=No", context=ai.DictContext())
                    text = await dude.ask(message.content)
                    await message.channel.send(text.text)
                    await dude.close()
                else:
                    return
                    
def setup(bot):
    bot.add_cog(AI(bot))