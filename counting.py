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


def get_base_x_distr(base, n_places=8):
    base_count = get_base_count(base, n_places)
    distr = {}

    for _, number in base_count.items():
        digit_sum = sum(number)

        if digit_sum not in distr:
            distr[digit_sum] = 1
        else:
            distr[digit_sum] += 1

    return distr

    


if __name__ == "__main__":

    numeric_system = ['dog', 'cat', 'bear']
    # print(dec_to_symbolic(32, numeric_syst=numeric_system, n_places=5))
    for k, v in get_base_count(numeric_system, n_places=3).items():
        print(f'{k}: {v}')