import sys
import discord

TOKEN = ''
f = open("token", "r")
TOKEN = f.read()
if TOKEN == '' :
    sys.exit("Token non défini")

client = discord.Client()

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    sys.stdout.flush()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'ping':
        await message.channel.send(f"__***----------------Je t'ai à l'oeil, {message.author.display_name}! 👀 ------------------***__")
        embed = discord.Embed(title="Forlas bot vous aide !!", description="Apprenez à utiliser discord", color=0xeee657)

        embed.add_field(name="Fermer Discord", value="ALT+F4 pour fermer discord ou sinon vous avez une croix en haut à droite", inline=False)
        embed.add_field(name="Ne pas parler", value="Si tu la ferme ça vaut mieux pour toi x)", inline=False)
        embed.add_field(name="Si vous avez un mac :", value="Acheter un windows !!", inline=False)
        embed.add_field(name="Les gens qui utilise H24 linux", value="Sachez que je vous soutiens pas", inline=False)

        await message.channel.send(embed=embed)
        return

client.run(TOKEN)