import discord
from discord import app_commands

########################## DISCLAIMER ##########################


# Use o comando /teste no final do processo para o discord reconhecer o bot como funcional 

# Você não precisa alterar NADA nesse código além das variáveis abaixo.
# Para conseguir esse id, basta clicar com botão direito no ícone do servidor, e depois em "copiar ID"

# Após copiar o ID, 
# cole-o aqui embaixo \/
id_do_servidor = Insira_seu_id_aqui



# O token do bot é como sua "identidade", e ao mesmo tempo sua "senha". Não mande para ninguém não confiável.
# Para conseguir o token do bot, você precisa criar um "perfil" para sua aplicação no link : https://discord.com/developers/applications
# Depois disso, vá até a aba Bot, e clique em Build-a-bot, e a página exibirá o token 
# que deve ser colado abaixo \/
bot_token = Insira_seu_token_aqui



# Após colocar as variáveis, apenas rode o arquivo, vá até o servidor que você conseguiu o ID ( ele só funciona lá ), e rode o comando /teste







# Pode ignorar tudo daqui pra baixo, já sujei minhas mãos por você :D




class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        #Checar se os comandos slash foram sincronizados 
        if not self.synced:
            # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            await tree.sync(guild = discord.Object(id=id_do_servidor)) 
            self.synced = True
        print(f"Entramos como {self.user}. \n Código do @studypyyyter no tiktok, e @lemeestudos no instagram :D")
aclient = client()
tree = app_commands.CommandTree(aclient)
@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Testando') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Parabéns, amigão. Eu estou funcionando!!!", ephemeral = True) 
aclient.run(bot_token)