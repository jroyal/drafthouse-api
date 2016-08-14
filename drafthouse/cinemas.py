from feed import get_feed
from films import Film
import json


def get_cinemas(market_id):
    cinemas = []
    feed = get_feed(market_id)
    for cinema in feed["Market"]["Dates"][0]["Cinemas"]:
        cinemas.append({
            "cinema_name": cinema["CinemaName"],
            "cinema_id": cinema["CinemaId"]
        })
    return cinemas


def get_cinema(cinema_id):
    print "Cinema ID:", cinema_id
    market_id = "{}00".format(cinema_id[:2])
    print "Market ID:", market_id
    feed = get_feed(market_id)
    for cinema in feed["Market"]["Dates"][0]["Cinemas"]:
        if cinema["CinemaId"] == cinema_id:
            films = []
            for film in cinema["Films"]:
                films.append(Film(film).__dict__)
            print films
            cinema["Films"] = films
            return cinema
    return None
