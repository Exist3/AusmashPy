from session_init import session

url_base = 'https://api.ausmash.com.au/'


class Character(object):
    def __init__(self, id):
        self.id = id

    @staticmethod
    def show_all():
        path = url_base + 'characters'
        response = session.get(path)
        return response.json()

    @staticmethod
    def by_game(game):
        path = url_base + 'characters/bygame/{}'.format(game.id)
        response = session.get(path)
        return response.json()

    @staticmethod
    def get_id_from_name(name, game_acronym):
        for result in Character.show_all():
            if name == result['Name'] and game_acronym == result['GameShort']:
                return result['ID']

    def info(self):
        path = url_base + 'characters/{}'.format(self.id)
        response = session.get(path)
        return response.json()

    def results(self):
        path = url_base + 'characters/{}/results'.format(self.id)
        response = session.get(path)
        return response.json()

    def matches(self):
        path = url_base + 'characters/{}/matches'.format(self.id)
        response = session.get(path)
        return response.json()

    def matches_won(self):
        path = url_base + 'characters/{}/matcheswins'.format(self.id)
        response = session.get(path)
        return response.json()

    def matches_lost(self):
        path = url_base + 'characters/{}/matcheslosses'.format(self.id)
        response = session.get(path)
        return response.json()

    def videos(self):
        path = url_base + 'characters/{}/videos'.format(self.id)
        response = session.get(path)
        return response.json()

    def players(self):
        path = url_base + 'characters/{}/players'.format(self.id)
        response = session.get(path)
        return response.json()


class Game(object):
    def __init__(self, id):
        self.id = id

    @staticmethod
    def show_all():
        path = url_base + 'games'
        response = session.get(path)
        return response.json()

    @staticmethod
    def get_id_from_acronym(acronym):
        for result in Game.show_all():
            if acronym == result['Short']:
                return result['ID']

    def info(self):
        path = url_base + 'games/{}'.format(self.id)
        response = session.get(path)
        return response.json()
