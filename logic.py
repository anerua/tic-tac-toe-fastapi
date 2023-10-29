"""
    Created: 29 October 2023 18:30
    Author: Martins Anerua

    Notes:
        1. A state is a particular unique game board
        2. state[9] represents the player whose turn it is to play (not the one whose play resulted in the current game state)
        3. Solitude is the Maximizer and human player is the Minimizer
"""

from typing import Tuple, List

import copy
import math


PLAY = 0
WIN = 1
LOSS = 2
DRAW = 3
ERROR = -1

def is_draw(state, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    mini : str
        The Minimizer player.
    maxi : str
        The Maximizer player.

    Returns
    -------
    bool
        Returns True if the game, as represented by state, is a draw and returns False otherwise.

    """ 
   
    if is_win(state, mini) or is_win(state, maxi):
        return False
    else:
        return '-' not in state

def is_win(state, player):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    player : str
        A string of one character, representing the player whose win status is to be checked.

    Returns
    -------
    bool
        Returns True if the game results in a win for player, and returns False if it doesn't.

    """
    condition1 = ((player == state[0]) and (player == state[1]) and (player == state[2]))
    condition2 = ((player == state[3]) and (player == state[4]) and (player == state[5]))
    condition3 = ((player == state[6]) and (player == state[7]) and (player == state[8]))
    condition4 = ((player == state[0]) and (player == state[3]) and (player == state[6]))
    condition5 = ((player == state[1]) and (player == state[4]) and (player == state[7]))
    condition6 = ((player == state[2]) and (player == state[5]) and (player == state[8]))
    condition7 = ((player == state[0]) and (player == state[4]) and (player == state[8]))
    condition8 = ((player == state[2]) and (player == state[4]) and (player == state[6]))
    return condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8

def is_a_way(state, player, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    player : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if there is ONLY one a way to win for player in the current game state. Returns False otherwise

    """
    if end_state(state, mini, maxi) or is_two_ways(state, player, mini, maxi):
        return False
    else:
        condition1 = (('-' == state[0]) and (player == state[1]) and (player == state[2])) or (
                (player == state[0]) and ('-' == state[1]) and (player == state[2])) or (
                             (player == state[0]) and (player == state[1]) and ('-' == state[2]))
        condition2 = (('-' == state[3]) and (player == state[4]) and (player == state[5])) or (
                (player == state[3]) and ('-' == state[4]) and (player == state[5])) or (
                             (player == state[3]) and (player == state[4]) and ('-' == state[5]))
        condition3 = (('-' == state[6]) and (player == state[7]) and (player == state[8])) or (
                (player == state[6]) and ('-' == state[7]) and (player == state[8])) or (
                             (player == state[6]) and (player == state[7]) and ('-' == state[8]))
        condition4 = (('-' == state[0]) and (player == state[3]) and (player == state[6])) or (
                (player == state[0]) and ('-' == state[3]) and (player == state[6])) or (
                             (player == state[0]) and (player == state[3]) and ('-' == state[6]))
        condition5 = (('-' == state[1]) and (player == state[4]) and (player == state[7])) or (
                (player == state[1]) and ('-' == state[4]) and (player == state[7])) or (
                             (player == state[1]) and (player == state[4]) and ('-' == state[7]))
        condition6 = (('-' == state[2]) and (player == state[5]) and (player == state[8])) or (
                (player == state[2]) and ('-' == state[5]) and (player == state[8])) or (
                             (player == state[2]) and (player == state[5]) and ('-' == state[8]))
        condition7 = (('-' == state[0]) and (player == state[4]) and (player == state[8])) or (
                (player == state[0]) and ('-' == state[4]) and (player == state[8])) or (
                             (player == state[0]) and (player == state[4]) and ('-' == state[8]))
        condition8 = (('-' == state[2]) and (player == state[4]) and (player == state[6])) or (
                (player == state[2]) and ('-' == state[4]) and (player == state[6])) or (
                             (player == state[2]) and (player == state[4]) and ('-' == state[6]))
        return condition1 or condition2 or condition3 or condition4 or condition5 or condition6 or condition7 or condition8
    
def is_two_ways(state, player, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    player : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if there are AT LEAST two ways to win for player in the current game state. Returns False otherwise

    """
    if end_state(state, mini, maxi):
        return False
    else:
        condition1 = (('-' == state[0]) and (player == state[1]) and (player == state[2])) or (
                (player == state[0]) and ('-' == state[1]) and (player == state[2])) or (
                             (player == state[0]) and (player == state[1]) and ('-' == state[2]))
        condition2 = (('-' == state[3]) and (player == state[4]) and (player == state[5])) or (
                (player == state[3]) and ('-' == state[4]) and (player == state[5])) or (
                             (player == state[3]) and (player == state[4]) and ('-' == state[5]))
        condition3 = (('-' == state[6]) and (player == state[7]) and (player == state[8])) or (
                (player == state[6]) and ('-' == state[7]) and (player == state[8])) or (
                             (player == state[6]) and (player == state[7]) and ('-' == state[8]))
        condition4 = (('-' == state[0]) and (player == state[3]) and (player == state[6])) or (
                (player == state[0]) and ('-' == state[3]) and (player == state[6])) or (
                             (player == state[0]) and (player == state[3]) and ('-' == state[6]))
        condition5 = (('-' == state[1]) and (player == state[4]) and (player == state[7])) or (
                (player == state[1]) and ('-' == state[4]) and (player == state[7])) or (
                             (player == state[1]) and (player == state[4]) and ('-' == state[7]))
        condition6 = (('-' == state[2]) and (player == state[5]) and (player == state[8])) or (
                (player == state[2]) and ('-' == state[5]) and (player == state[8])) or (
                             (player == state[2]) and (player == state[5]) and ('-' == state[8]))
        condition7 = (('-' == state[0]) and (player == state[4]) and (player == state[8])) or (
                (player == state[0]) and ('-' == state[4]) and (player == state[8])) or (
                             (player == state[0]) and (player == state[4]) and ('-' == state[8]))
        condition8 = (('-' == state[2]) and (player == state[4]) and (player == state[6])) or (
                (player == state[2]) and ('-' == state[4]) and (player == state[6])) or (
                             (player == state[2]) and (player == state[4]) and ('-' == state[6]))
        conditions = [condition1, condition2, condition3, condition4, condition5, condition6, condition7, condition8]
        return conditions.count(True) > 1

def end_state(state, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    mini : str
        The Minimizer player.
    maxi : str
        The Maximizer player.

    Returns
    -------
    bool
        Returns True if the state is a win state for any player or a draw state. Returns False otherwise.

    """
    return is_draw(state, mini, maxi) or is_win(state, mini) or is_win(state, maxi)

def has_center(state, focus):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    focus : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if 'focus' is present in the center position of 'state'. Returns False otherwise.

    """
    return state[4] == focus

def has_corner(state, focus):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    focus : str
        A string of one character, representing the player whose status is to be checked.

    Returns
    -------
    bool
        Returns True if 'focus' is present in at least one of the corner positions of 'state'. Returns False otherwise.

    """
    return (state[0] == focus) or (state[2] == focus) or (state[6] == focus) or (state[8] == focus)

def static_value(state, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    mini : str
        The Minimizer player.
    maxi : str
        The Maximizer player.

    Returns
    -------
    value : int
        Returns the static value of 'state'. This ranges from +100 to -100 inclusively.

    """
    value = 0
    if is_win(state, maxi):
        value = 100
    else:
        if is_win(state, mini):
            value = -100
        else:
            if is_draw(state, mini, maxi):
                value = 0
            else:
                if is_two_ways(state, maxi, mini, maxi):
                    value += 50
                if is_a_way(state, maxi, mini, maxi):
                    value += 10
                if has_center(state, maxi):
                    value += 5
                if has_corner(state, maxi):
                    value += 1
                
                if is_two_ways(state, mini, mini, maxi):
                    value -= 50
                if is_a_way(state, mini, mini, maxi):
                    value -= 10
                if has_center(state, mini):
                    value -= 5
                if has_corner(state, mini):
                    value -= 1
    return value

def get_all_next_moves(state, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    mini : str
        The Minimizer player.
    maxi : str
        The Maximizer player.

    Returns
    -------
    moves : list
        Returns a list of all valid possible states that differ from 'state' by one move.

    """
    moves = []
    if end_state(state, mini, maxi):
        return moves
    else:
        indices = []
        for _ in range(9):
            if state[_] == '-':
                indices.append(_)
        player = copy.deepcopy(state[9])
        for index in indices:
            temp_state = copy.deepcopy(state)
            temp_state[index] = player
            if player == maxi:
                temp_state[9] = mini
            elif player == mini:
                temp_state[9] = maxi
            moves.append(temp_state)
        return moves

def minimax(state, depth, alpha, beta, mini, maxi):
    """
    

    Parameters
    ----------
    state : list
        A list of length 10, representing a particular state of the game.
    depth : int
        The depth of the search tree.
    alpha : int
        Alpha value.
    beta : TYPE
        Beta value.
    mini : str
        The Minimizer player.
    maxi : str
        The Maximizer player.

    Returns
    -------
    list
        Implements the minimax algorithm with alpha-beta pruning and 
        returns a list whose first index is the alpha/beta value of the game state 
        and the second index is another list representing the next state recommended
        by the algorithm.

    """
    if end_state(state, mini, maxi) or depth == 0:
        return [static_value(state, mini, maxi), ""]
    next_moves = get_all_next_moves(state, mini, maxi)
    move = []
    if state[9] == maxi:
        for s in next_moves:
            score = minimax(s, depth - 1, alpha, beta, mini, maxi)[0]
            if score > alpha:
                move = copy.deepcopy(s)
                alpha = score
            if alpha >= beta:
                break
        return [alpha, move]
    elif state[9] == mini:
        for s in next_moves:
            score = minimax(s, depth - 1, alpha, beta, mini, maxi)[0]
            if score < beta:
                move = copy.deepcopy(s)
                beta = score
            if alpha >= beta:
                break
        return [beta, move]

def avail_position(state):
    """
    

    Parameters
    ----------
    game : list
        A list of length 10, representing a particular state of the game.

    Returns
    -------
    avail : list
        Returns a list of all available positions in state.

    """
    avail = []
    for _ in range(0,9):
        if state[_] == '-':
            avail.append(_)
    return avail

def play(state: List[str], mini: str, maxi: str) -> Tuple[List[str], int]:
    if not end_state(state, mini, maxi):
        ai_move = minimax(state, 2, -math.inf, math.inf, mini, maxi)[1]
        if not end_state(ai_move, mini, maxi):
            # return ai_move and PLAY
            return ai_move, PLAY
        elif is_win(ai_move, maxi):
            # return ai_move and WIN
            return ai_move, WIN
        elif is_draw(ai_move, mini, maxi):
            # return ai_move and DRAW
            return ai_move, DRAW
        else:
            # Scary. Hope we never get here
            return ai_move, ERROR
    else:
        if is_win(state, mini):
            # return state and LOSS
            return state, LOSS
        elif is_win(state, maxi):
            # this condition shouldn't run
            return state, ERROR
        else:
            # return state and DRAW
            return state, DRAW