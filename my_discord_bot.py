from ast import List
import sys
from unicodedata import category
import discord
from discord_components import DiscordComponents, ComponentsBot, Button, Select, SelectOption

TOKEN = ''
f = open("token", "r")
TOKEN = f.read()
if TOKEN == '' :
    sys.exit("Token non défini")


bot = ComponentsBot(command_prefix = "!")
notreListDevoir = []


@bot.command(name='manageDevoir')
async def manage_devoir(ctx):
    await ctx.channel.send(
        "OH! Tu as du travail à faire ?",
        components = [
            Button(label = "Oui! Je veux l'ajouter à ma liste STP !", custom_id = "button1")
        ]
    )

    interaction = await bot.wait_for("button_click", check = lambda i: i.custom_id == "button1")
    await interaction.send(
        "Voici ce que je peux faire pour toi :", 
        components = [
            Select(
                placeholder = "clique-ici pour voir ce que tu peux faire",
                options = [
                    SelectOption(label = "Ajouter un devoir", value = "option_1"),
                    SelectOption(label = "Modifier un devoir", value = "option_2"),
                    SelectOption(label = "Supprimer un devoir", value = "option_3"),
                ]
            )
        ]
    )

    interaction = await bot.wait_for("select_option")
    res = interaction.values[0]

    if res == "option_3":
        if len(notreListDevoir) > 0:
            embed = discord.Embed(title="Voici vos devoirs actuel:", color=0xeee657)
            for i in range(len(notreListDevoir)):
                embed.add_field(name=str(notreListDevoir[i]), value="Index n°"+ str(i), inline=False)
            await ctx.send(embed=embed)

            find = False

            while find ==False :
                await interaction.send(content = f"*Entre l'index de ton devoir à supprimer*")
                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel
                msg = await bot.wait_for("message", check=check)
                if (msg.content).isdecimal() == True :
                    if int(msg.content) < len(notreListDevoir):                
                        await ctx.send(content = f"*Vous avez choisi de supprimer le devoir n°"+str(msg.content)+"*")
                        del notreListDevoir[int(msg.content)]
                        find = True
                    else :
                        await ctx.send(content = f"*Cet index n'existe pas ! Essaye à nouveau :*")
                else:
                    await ctx.send(content = f"*Ton message doit contenir uniquement un chiffre, réessaye :*")  
        else :
            await ctx.send("*Vous n'avez pas de devoir !*")

    elif res == "option_2":
        if len(notreListDevoir) > 0:
            embed = discord.Embed(title="Voici vos devoirs actuel:", color=0xeee657)
            for i in range(len(notreListDevoir)):
                embed.add_field(name=str(notreListDevoir[i]), value="Index n°"+ str(i), inline=False)
            await ctx.send(embed=embed)

            find = False

            while find ==False :
                await interaction.send(content = f"*Entre l'index de ton devoir à modifier :*")
                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel
                msg = await bot.wait_for("message", check=check)
                if (msg.content).isdecimal() == True :
                    if int(msg.content) < len(notreListDevoir):                
                        await ctx.send(content = f"*Vous avez choisi de modifier le devoir n°"+str(msg.content)+"*")
                        await ctx.send(content = f"*Entre le nouveau titre pour remplacer l'ancien*")
                        msg2 = await bot.wait_for("message", check=check)
                        notreListDevoir[int(msg.content)] = str(msg2.content)
                        await ctx.send(content = f"*Titre bien modifier !*")
                        find = True
                    else :
                        await ctx.send(content = f"*Cet index n'existe pas ! Essaye à nouveau :*")
                else:
                    await ctx.send(content = f"*Ton message doit contenir uniquement un chiffre, réessaye :*")  
        else :
            await ctx.send("*Vous n'avez pas de devoir !*")


    elif res == "option_1":
        await interaction.send(content = f"*Entre un devoir à ajouter*")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await bot.wait_for("message", check=check)
       
        notreListDevoir.append(msg.content)
        await ctx.send("*Vous avez ajouté le devoir : " + msg.content+"*")
        await ctx.send("*Voici votre liste de devoir actuel " + str(notreListDevoir)+"*")

@bot.command(name='devoir')
async def display_devoir(ctx):

    if len(notreListDevoir) > 0:
        embed = discord.Embed(title="Voici vos devoirs :", color=0xeee657)
        for i in range(len(notreListDevoir)):
            embed.add_field(name=str(notreListDevoir[i]), value="Devoir n°"+ str(i+1), inline=False)
        await ctx.send(embed=embed)
    else :
        await ctx.send("Vous n'avez pas de devoir !")

# @bot.command(name='setup')
# async def new(ctx):
#     guild = ctx.message.guild
#     nameCategory = "Devoirs-BOT"
#     nameChannel1 = "Vos Devoirs"
#     nameChannel2 = "bot-suggestion-upgrade"
#     await ctx.send(content = f"*Création de la catégorie*")
#     await guild.create_category(str(nameCategory))
#     cat = discord.utils.get(ctx.guild.categories, name=str(nameCategory))
#     await guild.create_text_channel(str(nameChannel1), category=cat)
#     await ctx.send(content = f"*Création du premier channel*")
#     await guild.create_text_channel(str(nameChannel2), category=cat)
#     await ctx.send(content = f"*Création du deuxième channel*")
#     channel1 = discord.utils.get(ctx.guild.channels, name=str(nameChannel1))
#     channel1_id = channel1.id
#     channel2 = discord.utils.get(ctx.guild.channels, name=str(nameChannel2))
#     channel2_id = channel2.id
#     await ctx.send(content = f"*Setup Fini*")
#     return channel1_id, channel2_id


bot.run(TOKEN)