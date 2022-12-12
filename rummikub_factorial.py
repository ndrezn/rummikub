import itertools
from functools import cache


def create_permutations(board):
    tile_orders = list(itertools.permutations(board))
    return tile_orders


@cache
def is_valid(possible_run):
    colors = [i[1] for i in possible_run]
    values = [i[0] for i in possible_run]

    if len(possible_run) < 3:
        return False

    # Identity set (different colors, same values)
    if len(set(colors)) == len(possible_run) and len(set(values)) == 1:
        return True

    # Consecutive set (same color, consecutive values)
    if (
        len(set(colors)) == 1
        and max(values) - min(values) == len(possible_run) - 1
        and len(set(values)) == len(possible_run)
    ):
        return True

    return False


def get_runs(unused_tiles, runs):
    # If we've used up all the tiles, we've found a solution
    if not unused_tiles:
        return runs, True
    tile_orders = create_permutations(unused_tiles)

    for i in range(0, len(tile_orders)):
        order = tile_orders[i]

        for i in range(0, len(board) + 1):
            if is_valid(order[0:i]):
                cur_runs = runs + [order[0:i]]
                cur_unused = [j for j in unused_tiles if j not in order[0:i]]

                # Recursive step... head down this branch and see if it's a solution
                cur_runs, is_solution = get_runs(cur_unused, cur_runs)

                # If we've found a valid set of runs end the loop
                if is_solution:
                    return cur_runs, True

    # If the loop completes it means it's a bust
    return runs, False


board = [
    (1, "y"),
    (3, "r"),
    (5, "r"),
    (6, "r"),
    (3, "r"),
    (4, "r"),
    (3, "y"),
    (3, "w"),
    (1, "r"),
    (1, "b"),
    (7, "r"),
]


print("Start:", board)
board = sorted(board, key=lambda i: (i[0], i[1]))
solution = get_runs(board, [])
print("Solution:", solution)
