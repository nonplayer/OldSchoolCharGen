import random
import systems
import math


def roll(num=1, size=6):
    die_num = num
    die_size = size
    total = 0
    for count in range(die_num):
        total += random.randint(1, die_size)
    return total


# def stats():
#     rolls = sorted([
#         roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6)
#     ])
#     # maybe add reverse=True ?
#     return rolls


def stats(rolls, numbs, sides):
    results = []
    while rolls > 0:
        results.append(roll(numbs, sides))
        rolls -= 1
    return sorted(results)


def get_mod(stat, modifier_range):
    num = int(stat)
    if modifier_range == 'classic':
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
    elif modifier_range == 'slim':
        mod = int((num - 10) / 3)
    elif modifier_range == 'modern':
        mod = math.floor((num - 10) / 2)
    else:
        mod = 0
    return mod


def get_standard_spread(array, spread, primes, modifier_range, racemods):
    # create the base dictionary:
    final = {}
    for i in spread:
        final.update({i: {'val': 0, 'mod': 0}})
    random.shuffle(primes)
    random.shuffle(spread)
    # separate the prime attributes from the mix first:
    for i in primes:
        spread.remove(i)
    my_stats = array
    for i in primes:
        num = int(my_stats.pop())
        if i in list(dict.keys(racemods)):
            num += racemods[i]
        final[i]['val'] = num
        final[i]['mod'] = get_mod(num, modifier_range)
    for i in spread:
        num = int(my_stats.pop())
        if i in list(dict.keys(racemods)):
            num += racemods[i]
        final[i]['val'] = num
        final[i]['mod'] = get_mod(num, modifier_range)
    return final


'''
>>> testd = {}
>>> testlist = ['a', 'b', 'c']
>>> for i in testlist:
...     testd.update({i: {'val': 1, 'mod': 2}})
'''


def main():
    import professions
    md = dict(professions.get_profession())
    sys_prefs = dict(systems.get_system_prefs('tnu'))
    primes = list(md['primAttr'])
    spread = list(sys_prefs['spread'])
    modrange = sys_prefs['modifier_range']
    for key, value in dict.items(get_standard_spread(spread, primes, modrange, {})):
        print(key, ":", value)


if __name__ == "__main__":
    main()
