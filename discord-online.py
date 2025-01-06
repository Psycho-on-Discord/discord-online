import discord
from discord.ext import tasks

# Erstelle einen Discord-Client
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Eingeloggt als {self.user}')
        
        # Setze den Status als "online" mit einer personalisierten Aktivität
        activity = discord.Game(name="Hier personalisierte aktivität")
        await self.change_presence(status=discord.Status.online, activity=activity)
        print("Status gesetzt. Ich bin online!")

# Füge hier deinen Token ein (als Benutzer-Token oder besser Bot-Token, falls möglich)
TOKEN = "DEIN_DISCORD_TOKEN_HIER"

client = MyClient()
client.run(TOKEN)
