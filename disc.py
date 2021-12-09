import discord
import os
import discord.ext
import random
list=["Привет","Приветики","Здорова","Здравки","Здравствуйте","Bonjour","Hola","*выжидающе молчит*","*кивает*","Guten Tag"]
client = discord.Client()
ran=len(list)
fillrandom = (random.randint(0,ran-1))
fill = list[int(fillrandom)]
class MyClient(discord.Client):
    async def on_ready(self):
       print("")
       print('Logged on as', self.user)
    async def on_message(self,message):
        role=message.guild.get_role(id роли)
        if message.content.startswith('что?'):
            await message.channel.send('Сам что')
        if role in message.author.roles:
            fillrandom = (random.randint(0,ran-1))
            fill = list[int(fillrandom)]
            await message.channel.send(fill)

client = MyClient()
client.run('токен')