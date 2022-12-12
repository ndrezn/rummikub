import itertools


def create_permutations(board):
    tile_orders = list(itertools.permutations(board))
    return tile_orders


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


def get_runs(tile_orders, sets, unused_tiles):
    if not unused_tiles:
        return sets, True
    if not tile_orders:
        return sets, False

    for i in range(0, len(tile_orders)):
        order = tile_orders[i]

        # Size counter doesn't work because our end contition will not continue
        for i in range(0, len(board) + 1):
            if is_valid(order[0:i]):
                new_sets = sets + [order[0:i]]

                new_tiles = order[i:]
                new_orders = create_permutations(new_tiles)
                new_unused = [j for j in unused_tiles if j not in order[0:i]]

                # Recursive step... head down this tree and see if
                # it is a valid solution.
                sol_sets, is_solution = get_runs(new_orders, new_sets, new_unused)

                if is_solution:
                    return sol_sets, True

    return sets, False


board = [
    (3, "r"),
    (4, "r"),
    (5, "r"),
    (6, "r"),
    (3, "r"),
    (3, "y"),
    (1, "w"),
    (3, "w"),
    (1, "y"),
    (1, "r"),
    (1, "b"),
]


print(board)

tile_orders = create_permutations(board)
solution = get_runs(tile_orders, [], board)

print(solution)
