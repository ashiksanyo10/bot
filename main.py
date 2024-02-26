from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from discord import Embed

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)
cids_count = 57
edc_count = 14

async def update_counts(channel, operation):
    global cids_count, edc_count

    if operation == '🦷':
        edc_count += 1
        await channel.send(f"**Ka-ching!** 💰\n"
                           f"Guess what? Another tooth decided to hide under the pillow and wait for the Tooth Fairy! 🦷🎉\n"
                           f"Now, our grand total of knocked-out teeth is {cids_count + edc_count}! Keep smiling! 😁🪥")
    elif operation == '🦴':
        edc_count -= 1
        await channel.send(f"**Oh snap!** 🤗\n"
                           f"No teeth extraction this time, but remember to brush well! 🪥🦷\n"
                           f"Total tooth knocked out is still {cids_count + edc_count}, keep shining those pearly whites! 😁🪥")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def hi(ctx):
    await ctx.send("Hey Cutie <3")
    
@bot.command()
async def info(ctx):
    await ctx.send("🌟✨ Hey there, Adorable Smiles! ✨🌈\n"
                   "I'm your Fluffy Tooth Fairy Bot, fluttering in to keep track of the whimsical tooth tales spun by our Dayana!💖\n"
                   "Get ready for a sprinkle of enchantment as we journey together through the magical realm of tooth extractions! 🌟🦷✨")

@bot.command()
async def total(ctx):
    total_count = cids_count + edc_count
    await ctx.send(f"🦄🌈 Tooth Count Update: {total_count}! Keep sparkling, little teeth! 😁✨")

@bot.command()
async def tap(ctx, operation):
    if operation == '🦷' or operation == '🦴':
        await update_counts(ctx.channel, operation)
    else:
        await ctx.send("🚫 Invalid operation. Use 🦷 to add or 🦴 to subtract.")

@bot.command(name='guide')
async def custom_help(ctx):
    embed = Embed(
        title="🌟✨ **Tooth Fairy Bot Commands** ✨🦷",
        description="Embark on this whimsical journey with the Tooth Fairy Bot 🌈🪥✨",
        color=0xFFD700  # You can set the color to something visually appealing
    )

    commands_list = [
        ("`!hi`", "Greet the tooth fairy bot with a cute message!🎀"),
        ("`!info`", "Learn about the magical tooth fairy bot and its purpose 💾"),
        ("`!total`", "Discover the total count of bravely departed teeth 💎"),
        ("`!tap 🦷`", "Increase the tooth count with a sprinkle of magic 👻"),
        ("`!tap 🦴`", "Decrease the tooth count, sometimes we make a mistake 😛!"),
        ("`!guide`", "Display this enchanting list of commands 🧰")
    ]

    for command, description in commands_list:
        embed.add_field(name=command, value=description, inline=False)

    await ctx.send(embed=embed)
    


bot.run(bt)
