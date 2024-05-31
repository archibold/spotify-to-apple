import os
from dotenv import load_dotenv
import applemusicpy

load_dotenv()

secret_key = os.getenv('APPLE_SECRET_KEY')
key_id = os.getenv('APPLE_KEY_ID')
team_id = os.getenv('APPLE_TEAM_ID')


am = applemusicpy.AppleMusic(secret_key=secret_key, key_id=key_id, team_id=team_id)
results = am.search('travis scott', types=['albums'], limit=5)
for item in results['results']['albums']['data']:
    print(item['attributes']['name'])