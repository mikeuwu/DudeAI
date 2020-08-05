#import aiosqlite
import discord

from discord.ext import commands
from json import load

class DudeAI(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="dude ", description="Discord Chat Bot")
        self.remove_command("help")

    async def on_connect(self):
        print("[INFO] - Connected to discord websocket gateway")

    async def on_ready(self):
        string = "[INFO] - DudeAI v1 Is started"
        print(string)
        print("-" * len(string))
        print("[INFO] - Used by {} guilds and {} users".format(len(self.guilds), len(self.users)))
        print("[INFO] - Websocket latency: {} ms".format(round(self.latency * 1000)))
        #self.db = await aiosqlite.connect("bot.db")
        #print("[INFO] - Database Setted up")
        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Spotify"))
        print("[INFO] - Setted bot status")
        self.load_extension("src.ai")
        print("[INFO] - Loaded src.ai module")

with open("botconfig.json", "r") as f:
    config = load(f)

bot = DudeAI()
bot.run(config["token"])
