# Update Alert Policy Channels

This script automatically updates all Alert policies with a user specified channel ID using the New Relic REST API.

>Note: [Admin User’s API Key](https://docs.newrelic.com/docs/apis/get-started/intro-apis/understand-new-relic-api-keys) is required.

The Notification channel IDs are accessible via the [`alerts_channels`](https://rpm.newrelic.com/api/explore/alerts_channels/list) endpoint:

```
curl -X GET 'https://api.newrelic.com/v2/alerts_channels.json' \
     -H 'X-Api-Key:{api_key}' -i 
```
 
The [`alerts_policy_channels`](https://rpm.newrelic.com/api/explore/alerts_policy_channels/update) endpoint updates policy/channel associations.

```
curl -X PUT 'https://api.newrelic.com/v2/alerts_policy_channels.json' \
     -H 'X-Api-Key:{api_key}' -i \
     -H 'Content-Type: application/json' \
     -G -d 'policy_id={policy_id}&channel_ids={channel_ids}' 
```

## Usage

To use, install the project requirements:

```
pip install -r requirements.txt
```

Update the `config.ini` with your New Relic Admin API Key and channel id. To get a list of Notification channel ids, you can run `get_notification_channels.py`

Then to update each policy:

```
python update_policies.py
```


