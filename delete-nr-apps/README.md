# delete-nr-apps

This script deletes all non-reporting applications from your New Relic APM dashboard. 

>Note: [Admin User’s API Key](https://docs.newrelic.com/docs/apis/get-started/intro-apis/understand-new-relic-api-keys) is required.

To use, update the `config.ini` with your New Relic Admin API Key.

Install the project requirements:

```
pip install -r requirements.txt
```

Then run:

```
python delete.py
```

