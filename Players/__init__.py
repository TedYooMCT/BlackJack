from .HumanPlayer import HumanPlayer as Human
from .RandomPlayer import RandomPlayer as Random
from .RLPlayers import QLOneStep, QLDecay
from .TablesPlayers import ExpectancyPlayer as Expectancy
from .TablesPlayers import BasicPlayer as Basic
__all__ = [
    QLOneStep,
    QLDecay,
    Human,
    Random,
    Expectancy,
    Basic
]
