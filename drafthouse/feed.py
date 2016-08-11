import requests
from cache import cache_market_feed, check_market_feed_cache
from consts import DRAFTHOUSE_BASE_URL, SHOWTIMES_BASE_URL
from markets import get_all_markets


def get_feed(market, force_update=False):
    feed = None if force_update else check_market_feed_cache(market)
    if feed is not None:
        return feed
    url = "{}/{}".format(SHOWTIMES_BASE_URL, market)
    r = requests.get(url)
    if r.status_code == 200:
        feed = r.json()
        cache_market_feed(market, feed)
    return feed


def process_feeds():
    for market in get_all_markets():
        get_feed(market["market_id"], force_update=True)


if __name__ == '__main__':
    print get_feed("dfw")
