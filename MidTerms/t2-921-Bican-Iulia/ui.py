from repository import Repository
from service import Service
import time


class UI:
    def __init__(self, service):
        self._service = service

    def qualifyingRound(self, players):
        print("----Qualifying Round----")
        # time.sleep(3)
        games, nPlayers = self._service.qualifying(players)
        winners = []
        for game in games:
            print("\nGame between:")
            print("P1:" + str(game[0]))
            print("P2:" + str(game[1]))
            # time.sleep(3)
            winner = int(input("Who wins? (1/2) >"))
            if winner == 1:
                game[0].Strength = game[0].Strength + 1
                winners.append(game[0])
            elif winner == 2:
                game[1].Strength = game[1].Strength + 1
                winners.append(game[1])
            else:
                raise Exception("Wrong player inputed!")
        # time.sleep(3)
        print("   ! Qualifying Done\n")
        return winners, nPlayers

    def playTournament(self, players):
        while len(players) != 1:
            n = len(players)
            if n == 2:
                print("---- Finals ----")
            else:
                print("----Last " + str(n) + "----")
            games, nPlayers = self._service.tournament(players)
            winners = []
            for game in games:
                print("\nGame between:")
                print("P1:" + str(game[0]))
                print("P2:" + str(game[1]))
                # time.sleep(3)
                winner = int(input("Who wins? (1/2) >"))
                if winner == 1:
                    game[0].Strength = game[0].Strength + 1
                    winners.append(game[0])
                elif winner == 2:
                    game[1].Strength = game[1].Strength + 1
                    winners.append(game[1])
                else:
                    raise Exception("Wrong player inputed!")
            # time.sleep(3)
            if n == 2:
                print("\n   ! Finals End ! ")
            else:
                print("\n   ! Last " + str(n) + " Done \n")
            players = winners
        print("Winner is " + str(players[0].Name) + " !!")
        return True

    def decideQualifying(self, n, players):
        if (n & (n - 1) == 0) and n != 0:  # it is power of 2 => no qualifying round
            try:
                return self.playTournament(players)
            except Exception as e:
                print(e)
        else:
            try:
                winners, nPlayersQualifications = self.qualifyingRound(players)
                newPlayers = players[:int(len(players)) - nPlayersQualifications * 2] + winners

                return self.playTournament(newPlayers)
            except Exception as e:
                print(e)

    def start(self):
        players = self._service.getAllSorted()
        print("     TENNIS TOURNAMENT     ")
        print("Players:")
        for player in players:
            print(str(player))
        n = len(players)  # number_players

        while True:
            ok = self.decideQualifying(n, players)
            if ok is True:
                break
