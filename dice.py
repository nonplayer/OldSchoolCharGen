import professions
import random
import systems


def roll(num=1, size=6):
    die_num = num
    die_size = size
    total = 0
    for count in range(die_num):
        total += random.randint(1, die_size)
    return total


def stats():
    rolls = sorted([
        roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6)
    ])
    # maybe add reverse=True ?
    return rolls


def get_mod(stat):
    num = int(stat)
    # mod = 0
    if num >= 18:
        mod = 3
    elif num >= 16:
        mod = 2
    elif num >= 13:
        mod = 1
    elif num >= 9:
        mod = 0
    elif num >= 6:
        mod = -1
    elif num >= 4:
        mod = -2
    else:
        mod = -3
    return mod


def get_spread(spread, primes):
    primes = list(primes)
    spread = list(spread)
    # create the base dictionary:
    final = {}
    for i in spread:
        final.update({i: {'val': 0, 'mod': 0}})
    random.shuffle(primes)
    random.shuffle(spread)
    # separate the prime attributes from the mix first:
    for i in primes:
            spread.remove(i)
    my_stats = stats()
    for i in primes:
        num = int(my_stats.pop())
        final[i]['val'] = num
        final[i]['mod'] = get_mod(num)
    for i in spread:
        num = int(my_stats.pop())
        final[i]['val'] = num
        final[i]['mod'] = get_mod(num)
    return final


'''
>>> testd = {}
>>> testlist = ['a', 'b', 'c']
>>> for i in testlist:
...     testd.update({i: {'val': 1, 'mod': 2}})
'''


def main():
    md = dict(professions.get_profession())
    sys_prefs = dict(systems.get_system_prefs('tnu'))
    primes = list(md['primAttr'])
    spread = list(sys_prefs['spread'])
    for key, value in dict.items(get_spread(spread, primes)):
        print(key, ":", value)


if __name__ == "__main__":
    main()
