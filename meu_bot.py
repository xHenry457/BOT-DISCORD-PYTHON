import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f'{message.author.name} As Regras do Servidor São:{os.linesep}1- Não Desrespeitar os Membros{os.linesep}2- Não Falar Sobre Terra Plana{os.linesep}3- Liberado Xingar o Gabriel')
        
    
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} Acabou de entrar no {guild.name}'
            await guild.system_channel.send(mensagem)
            
intents = discord.Intents.default()
intents.members = True            

client = MyClient(intents=intents)
client.run('OTM4ODE1NjczODk3OTk2Mzc4.YfvyOw.PwT4ywk3Q6AKYlvXtpq16C8fyzk')