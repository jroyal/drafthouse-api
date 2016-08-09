import re
import json
import os
from bs4 import BeautifulSoup
import requests
from consts import DRAFTHOUSE_MARKETS, DRAFTHOUSE_BASE_URL
from multiprocessing.pool import ThreadPool
from cache import cache_markets, check_cache_market


class Market:
    def __init__(self, name, short_name, market_id):
        self.name = name
        self.short_name = short_name
        self.market_id = market_id or "Unknown"

    def __repr__(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def _get_market_id(market_short_name):
    market_id = None
    url = "{}/{}".format(DRAFTHOUSE_BASE_URL, market_short_name)
    r = requests.get(url, timeout=5)
    if r.status_code != 200:
        return market_id

    matches = re.search('marketUID\': \'(\d{4})\'', r.content)
    if matches:
        market_id = matches.group(1)
    return market_id


def update_market_cache():
    results = []
    r = requests.get(DRAFTHOUSE_MARKETS)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    markets = [(m.text, m.attrs["data-market"]) for m in soup.find_all("a", id="markets-page")]
    print markets
    pool = ThreadPool(20)
    markets = zip(markets, pool.map(_get_market_id, [m[1] for m in markets]))
    pool.close()
    pool.join()
    print markets

    for m in markets:
        results.append(Market(m[0][0], m[0][1], m[1]))

    market_json = json.dumps(results, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    cache_markets(market_json)
    return market_json


def get_all_markets():
    """
    Return a list of all markets the alamo drafthouse is in
    :return: List of markets
    """
    markets = []
    try:
        markets = check_cache_market() or update_market_cache()
    except Exception as e:
        print e
        markets = []

    return markets


if __name__ == '__main__':
    print get_all_markets()
