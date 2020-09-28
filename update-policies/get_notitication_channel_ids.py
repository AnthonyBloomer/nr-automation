import requests
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

ADMIN_API_KEY = config['default']['admin_api_key']
CHANNEL_ID = config['default']['channel_ids']

API_HEADER = {
    'X-Api-Key': ADMIN_API_KEY,
    'Content-Type': 'application/json'
}
req = requests.get('https://api.newrelic.com/v2/alerts_channels.json', headers=API_HEADER)

if not req.ok:
    req.raise_for_status()

channels = req.json()

for channel in channels['channels']:

    print("Id {}, name {}".format(channel['id'], channel['name']))
