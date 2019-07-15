from session_init import session

url_base = 'https://api.ausmash.com.au/'


class IncorrectArgumentsError(Exception):
    pass


class Character(object):
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.game_id = -1
        self.colour = ''
        self.icon_url = ''
        self.css_url = ''
        self.match_count = -1
        self.result_count = -1
        self.player_count = -1
        self.update()

    @staticmethod
    def get_characters(game=None):
        if game is None:
            path = url_base + 'characters'
        else:
            path = url_base + 'characters/bygame/{}'.format(game.id)
        response = session.get(path)
        return response.json()

    @staticmethod
    def get_character(name=None, game=None, id=None):
        if id is None and name is not None and game is not None:
            for result in Character.get_characters(game):
                if name == result['Name']:
                    return result
        elif id is not None and name is None and Game is None:
            path = url_base + 'characters/bygame/{}'.format(id)
            response = session.get(path)
            return response.json()
        else:
            raise IncorrectArgumentsError(
                "Character.get_character should only be executed with "
                "a name and game or a lone id"
            )

    def update(self):
        path = url_base + 'characters/{}'.format(self.id)
        response = session.get(path).json()
        self.name = response['Name']
        self.game_id = response['GameID']
        self.colour = response['Colour']
        self.icon_url = response['IconUrl']
        self.css_url = response['CssUrl']
        self.match_count = response['MatchCount']
        self.result_count = response['ResultCount']
        self.player_count = response['PlayerCount']

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
        self.name = ''
        self.short = ''
        self.update()

    @staticmethod
    def get_games():
        path = url_base + 'games'
        response = session.get(path)
        return response.json()

    @staticmethod
    def get_game(id=None, short=None, name=None):
        if sum(x is not None for x in (id, short, name)) != 1:
            raise IncorrectArgumentsError(
                "Game.get_game should only be executed with "
                "one argument."
            )
        elif id is not None:
            path = url_base + 'games/{}'.format(id)
            response = session.get(path)
            return response.json()
        elif short is not None:
            for result in Game.get_games():
                if short == result['Short']:
                    return result.json()
        elif name is not None:
            for result in Game.get_games():
                if name == result['Name']:
                    return result.json()

    def update(self):
        path = url_base + 'games/{}'.format(self.id)
        response = session.get(path).json()
        self.name = response['Name']
        self.short = response['Short']


class Player(object):
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.region_short = ''
        self.region_id = ''
        self.personal_url = ''
        self.twitch_url = ''
        self.youtube_url = ''
        self.twitter_url = ''
        self.facebook_url = ''
        self.ssb_world_url = ''
        self.bio = ''
        self.tournament_count = -1
        self.match_count = -1
        self.result_count = -1
        self.video_count = -1
        self.update()

    @staticmethod
    def get_players(region=None):
        if region is None:
            path = url_base + 'players'
        else:
            path = url_base + 'players/byregion/{}'.format(region.name)
        response = session.get(path)
        return response.json()

    @staticmethod
    def get_player(name=None, region=None, id=None):
        if id is None and name is not None and region is not None:
            path = url_base + 'players/find/{}/{}'.format(name, region.name)
        elif id is not None and name is None and region is None:
            path = url_base + 'players/{}'.format(id)
        else:
            raise IncorrectArgumentsError(
                "Player.get_player should only be executed with "
                "a name and region or a lone id"
            )
        response = session.get(path)
        return response.json()

    def update(self):
        path = url_base + 'players/{}'.format(self.id)
        response = session.get(path).json()
        self.name = response['Name']
        self.region_short = response['RegionShort']
        self.region_id = response['RegionID']
        self.personal_url = response['PersonalUrl']
        self.twitch_url = response['TwitchUrl']
        self.youtube_url = response['YouTubeUrl']
        self.twitter_url = response['TwitterUrl']
        self.facebook_url = response['FacebookUrl']
        self.ssb_world_url = response['SSBWorldUrl']
        self.bio = response['Bio']
        self.tournament_count = response['TournamentCount']
        self.match_count = response['MatchCount']
        self.result_count = response['ResultCount']
        self.video_count = response['VideoCount']

    def get_elo(self):
        path = url_base + 'players/{}/elo'.format(self.id)
        response = session.get(path)
        return response.json()

    def get_trueskill(self):
        path = url_base + 'players/{}/trueskill'.format(self.id)
        response = session.get(path)
        return response.json()

    def get_results(self):
        path = url_base + 'players/{}/results'.format(self.id)
        response = session.get(path)
        return response.json()

    def get_matches(self):
        path = url_base + 'players/{}/matches'.format(self.id)
        response = session.get(path)
        return response.json()

    def get_rankings(self):
        path = url_base + 'players/{}/rankings'.format(self.id)
        response = session.get(path)
        return response.json()

    def get_videos(self, character=None):
        if character is not None:
            path = url_base + 'players/{}/videos/{}'.format(self.id, character.id)
        else:
            path = url_base + 'players/{}/videos'.format(self.id)
        response = session.get(path)
        return response.json()

    def get_winrates(self, game):
        path = url_base + 'players/{}/winrates/{}'.format(self.id, game.id)
        response = session.get(path)
        return response.json()

    # Compare
    #def compare_stats(self, player, game):


class Region(object):
    def __init__(self, id):
        self.id = id
        self.name = ''
        self.short = ''
        self.update()

    @staticmethod
    def get_regions():
        path = url_base + 'regions'
        response = session.get(path)
        return response.json()

    @staticmethod
    def get_region(id):
        path = url_base + 'regions/{}'.format(id)
        response = session.get(path)
        return response.json()

    def update(self):
        path = url_base + 'regions/{}'.format(self.id)
        response = session.get(path).json()
        self.name = response['Name']
        self.short = response['Short']
