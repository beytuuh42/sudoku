

# Boards
BOARD_ZEROES = [[0 for _ in range(9)] for _ in range(9)]
BOARD = [[0, 6, 0, 2, 0, 0, 8, 3, 1],
         [0, 0, 0, 0, 8, 4, 0, 0, 0],
         [0, 0, 7, 6, 0, 3, 0, 4, 9],
         [0, 4, 6, 8, 0, 2, 1, 0, 0],
         [0, 0, 3, 0, 9, 6, 0, 0, 0],
         [1, 2, 0, 7, 0, 5, 0, 0, 6],
         [7, 3, 0, 0, 0, 1, 0, 2, 0],
         [8, 1, 5, 0, 2, 9, 7, 0, 0],
         [0, 0, 0, 0, 7, 0, 0, 1, 5]]

BOARD_FINISHED = [[0, 3, 4, 6, 7, 8, 9, 1, 2],
                  [6, 7, 2, 1, 9, 5, 3, 4, 8],
                  [1, 9, 8, 3, 4, 2, 5, 6, 7],
                  [8, 5, 9, 7, 6, 1, 4, 2, 3],
                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                  [9, 6, 1, 5, 3, 7, 2, 8, 4],
                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                  [3, 4, 5, 2, 8, 6, 1, 7, 9]]

BOARD_XWING1 = [[9, 8, 0, 0, 6, 2, 7, 5, 3],
                [0, 6, 5, 0, 0, 3, 0, 0, 0],
                [3, 2, 7, 0, 5, 0, 0, 0, 6],
                [7, 9, 0, 0, 3, 0, 5, 0, 0],
                [0, 5, 0, 0, 0, 9, 0, 0, 0],
                [8, 3, 2, 0, 4, 5, 0, 0, 9],
                [6, 7, 3, 5, 9, 1, 4, 2, 8],
                [2, 4, 9, 0, 8, 7, 0, 0, 5],
                [5, 1, 8, 0, 2, 0, 0, 0, 7]]


BOARD_XWING2 = [[0, 4, 1, 7, 2, 9, 0, 3, 0],
                [7, 6, 9, 0, 0, 3, 4, 0, 2],
                [0, 3, 2, 6, 4, 0, 7, 1, 9],
                [4, 0, 3, 9, 0, 0, 1, 7, 0],
                [6, 0, 7, 0, 0, 4, 9, 0, 3],
                [1, 9, 5, 3, 7, 0, 0, 2, 4],
                [2, 1, 4, 5, 6, 7, 3, 9, 8],
                [3, 7, 6, 0, 9, 0, 5, 4, 1],
                [9, 5, 8, 4, 3, 1, 2, 6, 7]]


BOARD_HIDDENPAIR_COLUMN = [[0, 4, 9, 1, 3, 2, 0, 0, 0],
                           [0, 8, 1, 4, 7, 9, 0, 0, 0],
                           [3, 2, 7, 6, 8, 5, 9, 1, 4],
                           [0, 9, 6, 0, 5, 1, 8, 0, 0],
                           [0, 7, 5, 0, 2, 8, 0, 0, 0],
                           [0, 3, 8, 0, 4, 6, 0, 0, 5],
                           [8, 5, 3, 2, 6, 7, 0, 0, 0],
                           [7, 1, 2, 8, 9, 4, 5, 6, 3],
                           [9, 6, 4, 5, 1, 3, 0, 0, 0]]


BOARD_HIDDENPAIR_BLOCK = [[0, 0, 0, 0, 6, 0, 0, 0, 0],
                          [0, 0, 0, 0, 4, 2, 7, 3, 6],
                          [0, 0, 6, 7, 3, 0, 0, 4, 0],
                          [0, 9, 4, 0, 0, 0, 0, 6, 8],
                          [0, 0, 0, 0, 9, 6, 4, 0, 7],
                          [6, 0, 7, 0, 5, 0, 9, 2, 3],
                          [1, 0, 0, 0, 0, 0, 0, 8, 5],
                          [0, 6, 0, 0, 8, 0, 2, 7, 1],
                          [0, 0, 5, 0, 1, 0, 0, 9, 4], ]

BOARD_PAIRS = [[1, 5, 0, 0, 0, 9, 8, 0, 4],
               [0, 0, 0, 3, 5, 8, 0, 2, 1],
               [0, 0, 0, 0, 0, 0, 0, 6, 0],
               [0, 0, 0, 0, 1, 0, 6, 7, 0],
               [0, 8, 0, 2, 0, 4, 0, 5, 0],
               [0, 1, 6, 0, 8, 0, 0, 0, 0],
               [0, 6, 0, 0, 0, 0, 0, 0, 0],
               [8, 9, 0, 5, 3, 7, 0, 0, 0],
               [7, 0, 1, 8, 0, 0, 0, 4, 5], ]
BOARD = BOARD_HIDDENPAIR_COLUMN


# Window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

GRID_WIDTH = WINDOW_WIDTH*0.9
GRID_HEIGHT = WINDOW_HEIGHT*0.9

GRID_SIZE = (GRID_WIDTH, GRID_HEIGHT)
GRID_POS = ((WINDOW_WIDTH / 2) - (GRID_WIDTH/2),
            (WINDOW_HEIGHT / 2) - (GRID_HEIGHT/2))

BLOCK_SIZE = [x/5 for x in GRID_SIZE]
BLOCK_WIDTH, BLOCK_HEIGHT = BLOCK_SIZE

CELL_SIZE = [x/3 for x in BLOCK_SIZE]
CELL_WIDTH, CELL_HEIGHT = CELL_SIZE

CANDIDATE_SIZE = [x/3 for x in CELL_SIZE]
CANDIDATE_WIDTH, CANDIDATE_HEIGHT = CANDIDATE_SIZE


# Colours

WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
LIGHTBLUE = (0, 136, 255)
RED = (220, 20, 60)