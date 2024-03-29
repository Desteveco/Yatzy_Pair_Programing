"""

Casos test de dfleta

"""

import pytest
from src.yatzy import Yatzy

@pytest.mark.chance
def test_chance():
    '''
    Chance
    The player scores the sum of all dice, no matter what they read.
    '''
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

@pytest.mark.yatzy
def test_yatzy():
    '''
    Yatzy
    If all dice have the same number, the player scores 50 points.
    '''
    # dice significa "dados" pero exige un unico argumento
    # => interfaz abstraccion del metodo no es coherente
    # con el resto de metodos
    # El codigo para iterar sobre dice es muy complejo
    # El algoritmo para averiguar si todos los dados son iguales
    # es muy complejo
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 1, 2)


# Ones, Twos, Threes, Fours, Fives, Sixes:
# The player scores the sum of the dice that reads one,
# two, three, four, five or six, respectively.

# Los metodos ones, twos, threes tienes codigo muy parecido:
# solo se diferencian en el numero que suman al total
# que es el numero de la categoria.
# Refactorizamos primero ones y luego exportamos
# la solucion a los demas.
# (mantener pasos pequenhos en la refactorizacion)
#
# Los algoritmos para iterar sobre la tirada de dados
# son muy complejos.

@pytest.mark.ones
def test_ones():
    '''
    The player scores the sum of the dice that reads one
    '''
    assert 0 == Yatzy.ones(3, 3, 3, 4, 5)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

@pytest.mark.twos
def test_twos():
    '''
    The player scores the sum of the dice that reads two
    '''
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)

@pytest.mark.threes
def test_threes():
    '''
    The player scores the sum of the dice that reads three
    '''
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)

# Los metodos fours, fives, sixes no son estaticos
# Necesitamos un objeto de la clase Yatzy
# Refactorizamos el constructor
# Estructura de datos: una lista, ya que es mutable
# y cada turno consta de 3 tiradas
# Las tuplas no son mutables. Refactorizo los metodos
# anteriores de tupla a lista <= no es necesario:
# ya que son estaticos y no emplean un objeto Yatzy

# La refactorizacion de los metodos fours, fives y sixes
# consiste en simplificar los algoritmos para recorrer
# la tirada de dados y sumar los puntos.

@pytest.fixture
def inyector():
    return (4, 5, 6, 4, 5)

@pytest.mark.fours
def test_fours(inyector):
    valorEsperado = 8
    resultado = Yatzy.fours(*inyector)
    assert valorEsperado == resultado

@pytest.mark.fives
def test_fives(inyector):
    '''
    The player scores the sum of the dice that reads five
    '''
    valorEsperado = 10
    resultado = Yatzy.fives(*inyector)
    assert valorEsperado == resultado

@pytest.mark.sixes
def test_sixes(inyector):
    '''
    The player scores the sum of the dice that reads six
    '''
    valorEsperado = 6
    resultado = Yatzy.sixes(*inyector)
    assert valorEsperado == resultado

@pytest.mark.score_pair
def test_score_pair():
    '''
    score_pair:
    The player scores the sum of the two highest matching dice.
    '''
    # El algoritmo del metodo no es optimo, es complicado e ilegible.
    # La abstraccion, el nombre del metodo, no es adecuada
    # puesto que la categoria se llama pair.
    assert 8 == Yatzy.score_pair(3, 3, 3, 4, 4)
    assert 12 == Yatzy.score_pair(1, 1, 6, 2, 6)
    assert 6 == Yatzy.score_pair(3, 3, 3, 4, 1)
    assert 6 == Yatzy.score_pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.score_pair(1, 2, 3, 4, 5)

@pytest.mark.pairs
def test_two_pair():
    '''
    Two pairs:
    If there are two pairs of dice with the same number, the
    player scores the sum of these dice.
    '''
    # La categoria se llama "two pairs": la abstraccion del metodo
    # no es adecuada.
    # Mantengo notacion snake_case
    # El algoritmo del metodo no es optimo, es complicado e ilegible.

    assert 8 == Yatzy.two_pair(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pair(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pair(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pair(1, 2, 3, 4, 5)


# Three of a kind:
# If there are three dice with the same number, the player
# scores the sum of these dice.
#
# El algoritmo del metodo no es optimo, es complicado e ilegible.

@pytest.mark.three_kind
def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 4, 5)
    assert 0 == Yatzy.three_of_a_kind(3, 3, 4, 5, 6)
    assert 9 == Yatzy.three_of_a_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_a_kind(1, 2, 3, 4, 5)

# Four of a kind:
# If there are four dice with the same number, the player
# scores the sum of these dice.
#
# El algoritmo del metodo no es optimo, es complicado e ilegible.

@pytest.mark.four_kind
def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_a_kind(2, 2, 2, 5, 5)
    assert 8 == Yatzy.four_of_a_kind(2, 2, 2, 2, 2)
    assert 0 == Yatzy.four_of_a_kind(1, 2, 3, 4, 5)

# Small straight:
# When placed on "small straight", if the dice read
#   1,2,3,4,5,
# the player scores 15 (the sum of all the dice).
#
# El nombre del metodo no es consistente con la nomenclatura snake_case
# El algoritmo es complicado e ineficiente.

@pytest.mark.small
def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.smallStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.smallStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.smallStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.smallStraight(1, 2, 3, 4, 6)


# Large straight:
# When placed on "large straight", if the dice read
#   2,3,4,5,6
# the player scores 20 (the sum of all the dice).
#
# El nombre del metodo no es consistente con la nomenclatura snake_case
# El algoritmo es complicado e ineficiente.

@pytest.mark.large
def largeStraight():
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.largeStraight(1, 3, 4, 5, 5)
    assert 0 == Yatzy.largeStraight(6, 6, 6, 6, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 3, 4, 6)


# Full house:
# If the dice are two of a kind and three of a kind, the
# player scores the sum of all the dice.

@pytest.mark.full
def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1, 1, 2, 2, 2)
    assert 0 == Yatzy.fullHouse(2, 2, 3, 3, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 4, 4)
    assert 0 == Yatzy.fullHouse(4, 4, 4, 1, 2)
