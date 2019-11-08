# https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem

def squares_needed(grains):
    
    if grains == 0:
        return 0
    
    square = 0
    while grains > 0:
        grains -= 2**square
        square += 1
    return square
