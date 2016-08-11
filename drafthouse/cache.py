import redis
import os
import json

HOST = os.getenv("DB_PORT_6379_TCP_ADDR", os.getenv("REDIS_HOST"))
PORT = os.getenv("DB_PORT_6379_TCP_PORT", "8090")
client = redis.StrictRedis(host=HOST, port=PORT, db=0)


def cache_markets(market_json):
    result = client.set("markets", market_json)
    if result:
        print "Successfully cached market information"
    else:
        print "Failed to cache market information"


def cache_market_feed(market, market_json):
    key = "market_{}".format(market)
    result = client.set(key, json.dumps(market_json))
    if result:
        print "Successfully cached market feed for {}".format(market)
    else:
        print "Failed to cache market information"


def check_cache_market():
    markets = client.get("markets")
    return json.loads(markets)


def check_market_feed_cache(market):
    market_json = client.get("market_{}".format(market))
    print market_json
    if market_json:
        return json.loads(market_json)
    else:
        return None
