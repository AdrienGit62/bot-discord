import sys
import discord

TOKEN = ''
f = open("token", "r")
TOKEN = f.read()
if TOKEN == '' :
    sys.exit("Token non défini")

client = discord.Client()

prefix = "!"

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == '{prefix}help':
        embed = discord.Embed(title="__***APPCLS vous donne les différentes commandes disponibles !!***__", description="", color=0xeee657)
        embed.add_field(name="Ajouter un devoir:", value="Tapez la commande : !add [titre_du_devoir]", inline=False)
        view = discord.ui.View()
        item = discord.ui.Button(style=discord.ButtonStyle.blurple, label="Click Me", url="https://google.com")
        view.add_item(item=item)
        await message.channel.send("This message has a button!", view=view)
        await message.channel.send(embed=embed)
        return



client.run(TOKEN)