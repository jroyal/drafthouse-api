import requests
import os
import json
import urllib
from datetime import datetime, date
from consts import DRAFTHOUSE_BASE_URL, SHOWTIMES_BASE_URL


def get_date_index(requested_date):
    requested_date = datetime.strptime(requested_date, "%m-%d-%Y").date()
    today = date.today()
    delta = requested_date - today
    return delta.days


def cache_feed_result(feed):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    today = date.today().strftime("%Y%m%d")
    filename = "{}-drafthousefeed.json".format(today)
    file_path = os.path.join(current_dir, "cache", filename)
    with open(file_path, "w+") as f:
        json.dump(feed, f)


def check_cache():
    feed = None
    current_dir = os.path.dirname(os.path.realpath(__file__))
    today = date.today().strftime("%Y%m%d")
    filename = "{}-drafthousefeed.json".format(today)
    file_path = os.path.join(current_dir, "cache", filename)
    if os.path.isfile(file_path):
        with open(file_path, "r+") as f:
            feed = json.load(f)
    return feed


def get_feed(market):
    feed = check_cache()
    if feed is not None:
        return feed
    url = "{}/{}".format(SHOWTIMES_BASE_URL, market)
    r = requests.get(url)
    if r.status_code == 200:
        feed = r.json()
        cache_feed_result(feed)
    return feed

if __name__ == '__main__':
    print get_feed("dfw")
