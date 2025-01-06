import discum  # Bibliothek für Benutzerkonten
import time

# Dein Discord-Token hier einfügen
TOKEN = "DEIN_DISCORD_TOKEN_HIER"

# Erstelle einen Client mit deinem Token
client = discum.Client(token=TOKEN, log=False)

# Funktion, um den Status zu aktualisieren
def set_status():
    client.setCustomStatus({"text": "Dein personalisierter Status"})  # Ändere den Status hier
    print("Status aktualisiert!")

# Einloggen und Verbindung aufrechterhalten
@client.gateway.command
def keep_alive(resp):
    if resp.event.ready_supplemental:  # Bei erfolgreicher Verbindung
        print(f"Eingeloggt als {client.gateway.session.user['username']}")
        set_status()

# Starte die Verbindung
client.gateway.run(auto_reconnect=True)

# Halte die Verbindung aktiv
while True:
    time.sleep(60)  # Halte das Skript am Laufen
