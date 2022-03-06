# search
import state
import frontier


def search(n):
    s = state.create(n)
    print(s)
    f = frontier.create(s)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[3]]
        ns = state.get_next(s)
        for i in ns:
            frontier.insert(f, i)
    return 0


if __name__ == "__main__":
    print(search(3))
