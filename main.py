from keep_alive import keep_alive
import discord
import random
import os
from discord.ext import commands
from discord import DMChannel
import string

client = commands.Bot(command_prefix = os.getenv('PREFIX')) 
client.remove_command('help')

link = "https://discord.gift/"
payam = 'Your Unlocked Nitro Code=>'

nitroEmbed=discord.Embed(title="Nitro Code Is Ready", url="https://discord.gg/vgnhGXabNw", description=f"Salam Baradar Man Baraie Shoma Link Nitro Gift Ro Estekhraj Kardam 🙂 , Lotfan Dm Khodra Check Konid Ta Linke Khodra Bebinid 🙂 Baraye Estefade Mojaddad Az Bot Commande Ro Be Ro Bezanid **{os.getenv('PREFIX')}gen**", color=discord.Color.blue())
nitroEmbed.set_footer(text="Created By Mr.SIN RE#1528")

#command Nitro ganerator
@client.command()
async def gen(ctx):
  if ctx.message.channel.id == (place-channel-id) or ctx.message.channel.id == (place-channel-id): #if you have some channel paste this code <or ctx.message.channel.id == (place-channel-id)> and enjoy 🙂
    user = await client.fetch_user(f"{ctx.author.id}")
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    number = list(string.digits)
    chars = lower + upper + number
    gen = "".join(random.choices(chars, k=16))
    await ctx.send(embed= nitroEmbed)
    await DMChannel.send(user,f"{payam + link + gen}")       

#command avatar 
@client.command()
async def avatar(ctx, member : discord.Member=None):
    if not member:
        member = ctx.author
    av_emb = discord.Embed(
        title = "Avatar Link 🔗",
        url = member.avatar_url,
        colour =discord.Color.random()
    )
    av_emb.set_author(
        name=f"{member}",
        icon_url=member.avatar_url
    )
    av_emb.set_footer(
        text=f"Requested by {ctx.author}",
        icon_url=ctx.author.avatar_url
    )
    av_emb.set_image(url=member.avatar_url)
    await ctx.send(embed=av_emb)

#command help
helpEmbed=discord.Embed(title="Nitro Bot Help Command", url="https://discord.gg/vgnhGXabNw", description="In Command Baraye Gereftane Kolle Command Haie Bote", color=discord.Color.random())
helpEmbed.set_footer(text="Created By Mr.SIN RE#1528 :)",icon_url="https://media.discordapp.net/attachments/880347850666545182/915858409738350602/image0-1_1.gif")
helpEmbed.add_field(name=f"**{os.getenv('PREFIX')}gen**" , value="sakht e code nitro" ,inline=False)
helpEmbed.add_field(name=f"**{os.getenv('PREFIX')}avatar**", value="gereftane avatar taraf", inline=False)
@client.command()
async def help(ctx):
  """kole command haie bot"""
  await ctx.send(embed = helpEmbed)


keep_alive()       
client.run(os.getenv('TOKEN'))
