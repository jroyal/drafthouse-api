import json


class Film(object):
    def __init__(self, film_json):
        self.id = film_json["FilmId"]
        self.name = film_json["FilmName"]
        self.year = film_json["FilmYear"]
        self.rating = film_json["FilmRating"]
        self.runtime = film_json["FilmRuntime"]
        # self.age_policy = film_json["FilmAgePolicy"]
        self.times = self._get_times(film_json["Series"])

    def _get_times(self, series):
        times = {}
        sessions = series[0]["Formats"][0]["Sessions"]
        for session in sessions:
            times[session["SessionTime"]] = session["SessionStatus"]
        return times
