def dec_to_base_x(dec, base, n_places=4):
    lst = []
    x = dec

    for _ in range(n_places):
        place = x % base
        lst.append(place)
        x //= base

    # print(lst[::-1] )
    return lst[::-1] 


def dec_to_symbolic(dec, numeric_syst, n_places):
    '''
    Note that our symbolic system has the left-most
    item in the list as equivalent to zero
    '''
    number_repr = dec_to_base_x(dec, base=len(numeric_syst), n_places=n_places)

    return [numeric_syst[x] for x in number_repr]


def get_base_count(numeric_syst, n_places=8):
    counts_d = {}

    for i in range(0, len(numeric_system)**n_places):
        counts_d[i] = dec_to_symbolic(i, numeric_system, n_places)
    
    return counts_d


def get_digit_sum(numeric_syst, number, symbolic):
    digit_sum_dec = []

    for item in number:
        digit_sum_dec.append(numeric_syst.index(item))

    if symbolic == False:
        return sum(digit_sum_dec)

    digit_sum_symbolic = dec_to_symbolic(sum(digit_sum_dec), numeric_syst, n_places=len(digit_sum_dec))

    digit_sum_symbolic = [str(item) for item in digit_sum_symbolic]

    return ''.join(digit_sum_symbolic)


def get_base_x_distr(numeric_syst, n_places=8, symbolic=True):
    base_count = get_base_count(numeric_syst, n_places)
    distr = {}

    for _, number in base_count.items():
        digit_sum = get_digit_sum(numeric_syst, number, symbolic=symbolic)

        if digit_sum not in distr:
            distr[digit_sum] = 1
        else:
            distr[digit_sum] += 1

    return distr

def simple_combinations(d):
    '''
    combinations of the current length of the counting system
    '''
    counts = d.values()
    perms = []

    for value in counts:
        perm = True

        for number in value:
            if value.count(number) > 1:
                perm = False
                break
        if perm == True and sorted(value, reverse=True) not in perms:
            perms.append(sorted(value, reverse=True))
    return sorted(perms)


if __name__ == "__main__":


    numeric_system = ['dog', 'cat', 'bear', 'elephant', 'pig']

    d = get_base_count(numeric_system, n_places=4)



    combs = simple_combinations(d)
    for comb in combs:
        print(comb)
    print(len(combs))