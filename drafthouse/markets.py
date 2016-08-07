import re
import json
import os
from bs4 import BeautifulSoup
import requests
from consts import DRAFTHOUSE_MARKETS, DRAFTHOUSE_BASE_URL
from multiprocessing.pool import ThreadPool


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


def update_market_info():
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

    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, "cache", "markets.json")
    with open(file_path, "w+") as markets_data:
        json.dump(results, markets_data, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def get_all_markets():
    """
    Return a list of all markets the alamo drafthouse is in
    :return: List of markets
    """
    try:
        current_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(current_dir, "cache", "markets.json")
        with open(file_path, "r") as markets_data:
            results = json.load(markets_data)
    except:
        results = []

    return results


if __name__ == '__main__':
    print get_all_markets()
