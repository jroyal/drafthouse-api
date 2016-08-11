from feed import get_feed


def get_cinemas(market_id):
    cinemas = []
    feed = get_feed(market_id)
    for cinema in feed["Market"]["Dates"][0]["Cinemas"]:
        cinemas.append({
            "cinema_name": cinema["CinemaName"],
            "cinema_id": cinema["CinemaId"]
        })
    return cinemas