import itertools


def get_pins(observed):
    str_key = str()
    key_dict = {
        '0': '08',
        '1': '124',
        '2': '2135',
        '3': '326',
        '4': '4157',
        '5': '25468',
        '6': '5639',
        '7': '748',
        '8': '50897',
        '9': '698',
    }

    if len(observed) == 0:
        return observed
    elif len(observed) == 1:
        key_list = []
        prev_key_list = list(itertools.combinations(key_dict[observed], len(observed)))
        for elem in prev_key_list:
            for el in elem:
                key_list.append(str(el))
        return key_list
    elif len(observed) == 2:
        final_lst = []
        first_str = key_dict[observed[0]]
        second_str = key_dict[observed[1]]
        for ch_1 in first_str:
            for ch_2 in second_str:
                fin_str = ch_1 + ch_2
                final_lst.append(fin_str)
        return final_lst

    elif len(observed) == 3:
        final_lst = []
        first_str = key_dict[observed[0]]
        second_str = key_dict[observed[1]]
        three_str = key_dict[observed[2]]
        for ch_1 in first_str:
            for ch_2 in second_str:
                for ch_3 in three_str:
                    fin_str = ch_1 + ch_2 + ch_3
                    final_lst.append(fin_str)
        return final_lst
    elif len(observed) == 4:
        final_lst = []
        first_str = key_dict[observed[0]]
        second_str = key_dict[observed[1]]
        three_str = key_dict[observed[2]]
        four_str = key_dict[observed[3]]
        for ch_1 in first_str:
            for ch_2 in second_str:
                for ch_3 in three_str:
                    for ch_4 in four_str:
                        fin_str = ch_1 + ch_2 + ch_3 + ch_4
                        final_lst.append(fin_str)
        return final_lst
print((get_pins('369')))