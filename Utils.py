def transform_record_into_dictionary(record):
    combinations = []
    for thing in record.split(":"):
        combinations.append(thing.split(" "))
    dict_event_combinations = {}
    combinations_A = []
    combinations_B = []
    combinations_C = []
    combinations_D = []
    combinations_E = []
    for combination in combinations:
        event = combination[0]
        if event == 'A':
            combinations_A.append(combination[1])
        elif event == 'B':
            combinations_B.append(combination[1])
        elif event == 'C':
            combinations_C.append(combination[1])
        elif event == 'D':
            combinations_D.append(combination[1])
        elif event == 'E':
            combinations_E.append(combination[1])
    dict_event_combinations['A'] = combinations_A
    dict_event_combinations['B'] = combinations_B
    dict_event_combinations['C'] = combinations_C
    dict_event_combinations['D'] = combinations_D
    dict_event_combinations['E'] = combinations_E
    return dict_event_combinations


def combine_event_value(event, record_dict):
    combined_list = []
    for value in record_dict[event[0]]:
        combined_list.append(event[0] + str(value))
    return combined_list


def get_numbers_from_str(string):
    num_list = []
    num = ''
    for char in string:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return num_list


def update_amounts(amounts, event):
    if event == 'A':
        amounts[0] += 1
    elif event == 'B':
        amounts[1] += 1
    elif event == 'C':
        amounts[2] += 1
    elif event == 'D':
        amounts[3] += 1
    elif event == 'E':
        amounts[4] += 1


def get_event_occurrence_amount(amounts, event):
    if event == 'A':
        return amounts[0]
    elif event == 'B':
        return amounts[1]
    elif event == 'C':
        return amounts[2]
    elif event == 'D':
        return amounts[3]
    elif event == 'E':
        return amounts[4]


def get_all_values(d):
    if isinstance(d, dict):
        for v in d.values():
            yield from get_all_values(v)
    elif isinstance(d, list):
        for v in d:
            yield from get_all_values(v)
    else:
        yield d


def get_event_number(event):
    if event[0] == 'A':
        return 0
    elif event[0] == 'B':
        return 1
    elif event[0] == 'C':
        return 2
    elif event[0] == 'D':
        return 3
    elif event[0] == 'E':
        return 4


def round_number(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num
