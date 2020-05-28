def dec_to_base_x(dec, base, n_places=4):
    lst = []
    x = dec

    for _ in range(n_places):
        place = x % base
        lst.append(place)
        x //= base

    return lst[::-1] 


def get_binary_in_range(n_places=8):
    counts_d = {}

    for i in range(0, 2**n_places):
        counts_d[i] = dec_to_binary(i, n_places)
    
    return counts_d



if __name__ == "__main__":
    print(dec_to_base_x(76, 7, n_places=10))

    # for k, v in get_binary_in_range(n_places=8).items():
    #     print(f'{k}: {v}')