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


def check_cache_market():
    markets = client.get("markets")
    return json.loads(markets)
