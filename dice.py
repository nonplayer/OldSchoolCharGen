import random

def roll(num=1, size=6):
    die_num = num
    die_size = size
    total = 0
    for count in range(die_num):
        total += random.randint(1, die_size)
    return(total)

def stats():
    spread = sorted([roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6), roll(3, 6)])  # maybe add?: , reverse=True
    return(spread)

def get_mod(stat):
    num = int(stat)
    mod = 0
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

def get_spread(system, PAs=''):
    final = {
        'CHA': {'val' : 0,'mod' : 0,},
        'DEX': {'val' : 0,'mod' : 0,},
        'FER': {'val' : 0,'mod' : 0,},
        'HEA': {'val' : 0,'mod' : 0,},
        'INT': {'val' : 0,'mod' : 0,},
        'WIL': {'val' : 0,'mod' : 0,},
    }
    primes = list(PAs)
    random.shuffle(primes)
    baseSpread = ['CHA', 'DEX', 'FER', 'HEA', 'INT', 'WIL', ]
    random.shuffle(baseSpread)
    for i in primes:
            baseSpread.remove(i)
    mySpread = stats()
    for i in primes:
        num = int(mySpread.pop())
        final[i]['val'] = num
        final[i]['mod'] = get_mod(num)
    for i in baseSpread:
        num = int(mySpread.pop())
        final[i]['val'] = num
        final[i]['mod'] = get_mod(num)
    return final


def main():
    for key, value in dict.items(get_spread('TNU',)):
        print(key, ":", value)

if __name__ == "__main__":
    main()
