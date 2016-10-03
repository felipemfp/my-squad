from enum import Enum
from itertools import permutations
from tabulate import tabulate


class Position(Enum):
    # Goalkeeper
    GK = 'Goalkeeper'

    # Defender
    SW = 'Sweeper'
    RB = 'Right Full-back'
    RWB = 'Right Wing-back'
    CB = 'Centre-back'
    LB = 'Left Full-back'
    LWB = 'Left Wing-back'

    # Midfielder
    DM = 'Defensive Midfield'
    CM = 'Centre Midfield'
    RM = 'Right Wide Midfield'
    LM = 'Left Wide Midfield'
    AM = 'Attacking Midfield'

    # Forward
    SS = 'Second Striker'
    CF = 'Centre Forward'
    RW = 'Right Winger'
    LW = 'Left Winger'


class Player(object):

    def __init__(self, name, position, age, rating=60, potencial=75):
        self.name = name
        self.position = position
        self.age = age
        self.potencial = potencial
        self.rating = rating

    def __repr__(self):
        return '<Player {}, {}>'.format(self.name, self.position.name)


class Squad(object):

    def __init__(self, players=[]):
        self.players = players

    def __repr__(self):
        return '<Squad with {} players>'.format(len(self.players))

    def players_details(self):
        data = [
            [
                player.position.name,
                player.name,
                player.age,
                player.rating,
                player.potencial
            ]
            for player in self.players]
        return tabulate(data, headers=('POS', 'NAME', 'AGE', 'RAT', 'POT'))


class Team(object):

    def __init__(self, name, squad, user_control=False):
        self.name = name
        self.squad = squad
        self.user_control = user_control

    def __repr__(self):
        return '<Team {}>'.format(self.name)


class TeamInLeague(object):

    def __init__(self, team, played=0, won=0, drawn=0, lost=0,
                 goals_for=0, goals_against=0):
        self.team = team
        self.played = played
        self.won = won
        self.drawn = drawn
        self.lost = lost
        self.goals_for = goals_for
        self.goals_against = goals_against

    def __repr__(self):
        return '<TeamInLeague {}>'.format(self.team.name)

    @property
    def points(self):
        return self.won * 3 + self.drawn * 1

    @property
    def goals_difference(self):
        return self.goals_for - self.goals_against


class League(object):

    def __init__(self, name, teams=[]):
        self.name = name
        self.teams = [TeamInLeague(team=team) for team in teams]
        self.matches = permutations(self.teams, 2)

    def __repr__(self):
        return '<League {}>'.format(self.name)

    def current_table(self):
        data = [
            (
                i + 1, team.team.name, team.played, team.won, team.drawn,
                team.lost, team.goals_for, team.goals_against,
                team.goals_difference, team.points
            )
            for i, team in enumerate(self.teams)]
        return tabulate(data, headers=('POS', 'TEAM', 'P', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'PTS'))
