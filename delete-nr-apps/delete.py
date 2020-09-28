import requests
import configparser
import asyncio
from urllib import parse
import sys
from aiohttp import ClientSession, ClientConnectorError

config = configparser.ConfigParser()
config.read('config.ini')

HEADERS = {
    'X-Api-Key': config['default']['admin_api_key']
}

API = 'https://api.newrelic.com/v2'

warn = "Are you sure you'd like to delete all non-reporting applications? " \
       "This is an irreversible process which will delete all reported data for each non-reporting application."

async def call(url: str, session: ClientSession) -> tuple:
    try:
        resp = await session.request(method="DELETE", url=url, headers=HEADERS)
    except ClientConnectorError:
        return url, 404
    return url, resp.status


async def make_requests(u: set) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in u:
            tasks.append(
                call(url=url, session=session)
            )
        results = await asyncio.gather(*tasks)

    for result in results:
        print(f'{result[1]} - {str(result[0])}')


if __name__ == "__main__":

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."

    urls = []

    if input("%s (y/N) " % warn).lower() == 'y':
        first = 1
        request = requests.head('%s/applications.json?page=%s' % (API, first), headers=HEADERS)
        
        if not request.ok:
            request.raise_for_status()
        
        last = int(parse.parse_qs(parse.urlparse(request.links['last']['url']).query)['page'][0]) if 'last' in request.links else first
        while first <= last:
            request = requests.get('%s/applications.json?page=%s' % (API, first), headers=HEADERS)
            json = request.json()
            applications = json['applications']
            print("Deleting applications...")
            for application in applications:
                if not application['reporting']:
                    urls.append('%s/applications/%s.json' % (API, application['id']))
            first += 1

    asyncio.run(make_requests(u=set(urls)))

    sys.exit(0)
