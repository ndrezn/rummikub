import itertools


def create_permutations(board):
    tile_orders = list(itertools.permutations(board))
    return tile_orders


def is_valid(possible_run):
    colors = [i[1] for i in possible_run]
    values = [i[0] for i in possible_run]

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


def get_runs(tile_orders, sets, size):
    if not tile_orders:
        return sets

    for i in range(0, len(tile_orders)):
        order = tile_orders[i]

        # Size counter doesn't work because our end contition will not continue
        for i in range(3, len(board) + 1):
            if is_valid(order[0:i]):
                new_sets = sets + [order[0:i]]
                tiles = order[i:]
                new_orders = create_permutations(tiles)
                if i == len(order):
                    return new_sets

                # Recursive step... head down this tree and see if
                # it is a valid solution.
                return get_runs(new_orders, new_sets, size)

    return sets


board = [
    (3, "r"),
    (3, "r"),
    (4, "r"),
    (5, "r"),
    (3, "y"),
    (3, "w"),
    (1, "y"),
    (1, "r"),
    (1, "b"),
]

tile_orders = create_permutations(board)
solution = get_runs(tile_orders, [], len(board))

print(solution)
