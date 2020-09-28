import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

ADMIN_API_KEY = config["default"]["admin_api_key"]
CHANNEL_ID = config["default"]["channel_ids"]

API_HEADER = {"X-Api-Key": ADMIN_API_KEY, "Content-Type": "application/json"}
req = requests.get(
    "https://api.newrelic.com/v2/alerts_policies.json", headers=API_HEADER
)

if not req.ok:
    req.raise_for_status()

policies = req.json()

for policy in policies["policies"]:
    data = {"policy_id": policy["id"], "channel_ids": CHANNEL_ID}
    req = requests.put(
        "https://api.newrelic.com/v2/alerts_policy_channels.json",
        headers=API_HEADER,
        json=data,
    )
    if not req.ok:
        req.raise_for_status()
    print("Policy updated.")
