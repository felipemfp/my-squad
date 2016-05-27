import names, click, math, random, pickle
from models import *

FILENAME = 'mysquad.sqd'

class MySquad(object):
    def __init__(self, team=None, league=None):
        self.current_team = team
        self.current_league = league

    def save(self):
        datafile = open(FILENAME, 'wb')
        with datafile:
            pickle.dump(self, datafile)

    @staticmethod
    def load():
        try:
            datafile = open(FILENAME, 'rb')
            with datafile:
                mySquad = pickle.load(datafile)
            if mySquad is None:
                return MySquad()
            return mySquad
        except FileNotFoundError:
            return MySquad()


    @staticmethod
    def generate_squad(count):
        squad = Squad(players=[])

        # default: 4-4-2
        gk = 1/11
        cb = 2/11
        fb = 2/11
        cm = 2/11
        am = 2/11
        cf = 2/11

        for x in range(0, math.ceil(count*gk)):
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.GK,
                age=random.randint(16, 35),
                rating=random.randint(50, 75),
                potencial=random.randint(60, 85)))
        for x in range(0, math.ceil(count*cb)):
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.CB, age=random.randint(16, 35),
                rating=random.randint(50, 80),
                potencial=random.randint(60, 90)))
        for x in range(0, math.ceil((count*fb)/2)):
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.RB, age=random.randint(16, 35),
                rating=random.randint(50, 80),
                potencial=random.randint(60, 85)))
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.LB, age=random.randint(16, 35),
                rating=random.randint(50, 80),
                potencial=random.randint(60, 85)))
        for x in range(0, math.ceil(count*cm)):
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.CM,
                age=random.randint(16, 35),
                rating=random.randint(50, 80),
                potencial=random.randint(60, 90)))
        for x in range(0, math.ceil(count*am)):
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.AM,
                age=random.randint(16, 35),
                rating=random.randint(50, 80),
                potencial=random.randint(60, 90)))
        for x in range(0, math.ceil(count*cf)):
            squad.players.append(Player(names.get_full_name(gender='male'),
                position=Position.CF,
                age=random.randint(16, 35),
                rating=random.randint(50, 90),
                potencial=random.randint(60, 99)))
        return squad


@click.group()
@click.pass_context
def cli(ctx):
    """
    MySquad is a CLI game about football (or soccer for Americans).

    More information: http://github.com/felipemfp/my-squad
    """
    click.clear()
    global mySquad
    mySquad = MySquad.load()


@cli.command('new')
@click.option('--name', prompt="Your team's name", help="Team's name that you are going to play with.")
def new_game(name):
    """
    Start a new game.

    You will lose the current progress.
    """
    global mySquad
    mySquad = MySquad()
    mySquad.current_team = Team(name, MySquad.generate_squad(18), user_control=True)
    mySquad.save()


@cli.command('save')
def save_game():
    """
    Save the game.

    Actually, it is unnecessary, because all actions save.
    """
    global mySquad
    mySquad.save()
    click.echo('Done.');


@cli.command('team')
def team():
    """
    Show the name of my current team.
    """
    click.echo('Playing with: {}.'.format(mySquad.current_team.name))


@cli.command('squad-details')
def squad_details():
    """
    Show details about my current squad.
    """
    click.echo("{}'s Squad:".format(mySquad.current_team.name))
    click.echo(mySquad.current_team.squad.players_details())


if __name__ == '__main__':
    cli()
