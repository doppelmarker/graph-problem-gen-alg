from Utils import transform_record_into_dictionary, round_number


def find_pivots():
    all_pivots = []
    file = open('BD.txt')
    for record in file:
        pivots = find_restrictions_pivots(record)
        all_pivots.append(pivots)
    average_pivots = [0, 0, 0, 0, 0]
    events_amounts = [0, 0, 0, 0, 0]
    for group_pivots in all_pivots:
        for key in group_pivots.keys():
            update_pivots(average_pivots, events_amounts, key, group_pivots[key])
    for i in range(len(average_pivots)):
        average_pivots[i] /= events_amounts[i]
    file.close()

    for i in range(len(average_pivots)):
        average_pivots[i] = round_number(average_pivots[i])

    return average_pivots


def find_restrictions_pivots(record):
    record_dict = transform_record_into_dictionary(record.rstrip())
    pivots = {}
    for key in record_dict.keys():
        average = 0
        for element in record_dict[key]:
            average += int(element)
        if len(record_dict[key]) > 0:
            average /= len(record_dict[key])
            pivots[key] = average
    return pivots


def update_pivots(average_pivots, events_amounts, event, pivot):
    if event == 'A':
        events_amounts[0] += 1
        average_pivots[0] += pivot
    elif event == 'B':
        events_amounts[1] += 1
        average_pivots[1] += pivot
    elif event == 'C':
        events_amounts[2] += 1
        average_pivots[2] += pivot
    elif event == 'D':
        events_amounts[3] += 1
        average_pivots[3] += pivot
    elif event == 'E':
        events_amounts[4] += 1
        average_pivots[4] += pivot
