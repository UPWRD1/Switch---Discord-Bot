import discord
import os
import googletrans
import discord.ext
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#import statements



description = "Switch is a multilingual translation and moderation bot, built for the purpose of easing communication."


#Bot Setup
intents = discord.Intents().all()
bot = commands.Bot(
	command_prefix="!", 
	case_insensitive=True, intents=intents
)

#Bot login
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

    


@bot.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"


@bot.command(aliases = ['tr'])
async def translate(ctx, lang_to, *args):
    """
    Translates the given text to the language `lang_to`.
    The language translated from is automatically detected.
    """

    lang_to = lang_to.lower()
    text = ' '.join(args)
    translator = googletrans.Translator()
    text_translated = translator.translate(text, dest=lang_to).text
    await ctx.reply(text_translated, mention_author=False)
    
bot.run(os.getenv('TOKEN'))
