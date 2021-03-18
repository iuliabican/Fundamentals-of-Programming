from repository import Repository, RepositoryError
import random

class Service:
    def __init__(self, repo):
        self._repo = repo

    def getAllSorted(self):
        players = self._repo.getAll()
        def sortStrength(val):
            return val.Strength

        players.sort(key=sortStrength, reverse=True)
        return players

    def qualifying(self, players):
        """
        Function that creates games for qualifications
        :param players: all the players in the game
        :return: the games that should be done between the players which need to go to qualifications
        """
        # here I calculate how many players we need to include in qualifications
        n = len(players)
        # get closest power of 2
        i = 1
        while i < n:
            i *= 2
        i = int(i / 2)
        # NplayersInQualifications is how many players are playing in qualifications
        NplayersInQualifications = (n-i)*2
        # select only the players that need qualifying (last in already sorted players list)
        playersInQualifications = players[n-NplayersInQualifications:]
        # shuffle them so we can get new games for the same input
        random.shuffle(playersInQualifications)

        # split in 2 groups then merge them
        group1 = playersInQualifications[:int(NplayersInQualifications/2)]
        group2 = playersInQualifications[int(NplayersInQualifications/2):]

        # merge the players to get games
        games = zip(group1, group2)
        return games, int(NplayersInQualifications/2)

    def tournament(self, players):
        """
        Function that creates games for tournament
        :param players: all the players in the game(previously checked to be exactly powers of 2)
        :return: the games that should be done between the (qualified) players
        """
        # get all players in the tournament
        playersInTournament = players

        # shuffle them so we can get new games for the same input
        random.shuffle(playersInTournament)
        nplayersInTournament = len(playersInTournament)

        # split in 2 groups then merge them
        group1 = playersInTournament[:int(nplayersInTournament / 2)]
        group2 = playersInTournament[int(nplayersInTournament / 2):]

        # merge the players to get games
        games = zip(group1, group2)
        return games, int(nplayersInTournament / 2)
