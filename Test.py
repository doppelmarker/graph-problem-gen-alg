import itertools
import random

import numpy as np

from Utils import *
from Pivots import find_pivots
import time
import copy
import matplotlib.pyplot as plt


def is_record_satisfied(graph, record):
    graph_original = {}
    for travel in graph:
        graph_original[travel[0]] = []
    for travel1 in graph:
        if len(graph_original[travel1[0]]) == 0:
            for travel2 in graph:
                if travel1[0] == travel2[0]:
                    graph_original[travel1[0]].append(travel2[1])

    record_dict = transform_record_into_dictionary(record.rstrip())
    total_travel_list = []
    for travel in graph:
        travel_list = [combine_event_value(travel[0], record_dict),
                       combine_event_value(travel[1], record_dict)]
        total_travel_list.append(list(itertools.product(*travel_list)))

    for i in range(len(total_travel_list)):
        interval_begin = graph[i][2]
        interval_end = graph[i][3]
        j = 0
        while j < len(total_travel_list[i]):
            event_with_number1 = total_travel_list[i][j][0]
            event_with_number2 = total_travel_list[i][j][1]
            point1 = get_numbers_from_str(event_with_number1)[0]
            point2 = get_numbers_from_str(event_with_number2)[0]
            distance = int(point2) - int(point1)
            if interval_begin > distance or distance > interval_end or event_with_number1 == event_with_number2:
                total_travel_list[i].pop(j)
                continue
            j += 1
        if len(total_travel_list[i]) == 0:
            return False

    all_routes = list(itertools.product(*total_travel_list))
    for route in all_routes:
        graph_remade = {}
        for travel in route:
            graph_remade[travel[0]] = []
        for travel1 in route:
            if len(graph_remade[travel1[0]]) == 0:
                for travel2 in route:
                    if travel1[0] == travel2[0]:
                        graph_remade[travel1[0]].append(travel2[1])

        temp = {}
        amounts = [0, 0, 0, 0, 0]
        for event in graph_remade.keys():
            if event not in temp:
                update_amounts(amounts, event[0])
                temp[event] = event[0] + '\'' * (get_event_occurrence_amount(amounts, event[0]) - 1)
            for elem in graph_remade[event]:
                if elem not in temp:
                    update_amounts(amounts, elem[0])
                    temp[elem] = elem[0] + '\'' * (get_event_occurrence_amount(amounts, elem[0]) - 1)

        for value in graph_remade.values():
            for i in range(len(value)):
                value[i] = temp[value[i]]
        graph_remade = {temp[k]: v for k, v in graph_remade.items()}

        if len(graph_original.keys()) != len(graph_remade.keys()):
            continue

        keys_ok = True
        for key_original, key_remade in zip(graph_original.keys(), graph_remade.keys()):
            if key_original != key_remade:
                keys_ok = False
                break

        if not keys_ok:
            continue

        all_values_original = list(get_all_values(graph_original))
        all_values_remade = list(get_all_values(graph_remade))
        len_original = len(all_values_original)
        len_remade = len(all_values_remade)

        if len_original != len_remade:
            continue

        counter = 0
        for i in range(min(len_original, len_remade)):
            if all_values_original[i] != all_values_remade[i]:
                break
            counter += 1

        if counter == len_original:
            return True

        # print(graph_remade)
    return False


def update_graph(event_number, existing_events, numbers_of_events):
    if event_number == 0:
        numbers_of_events[0] += 1
        existing_events.append("A" + '\'' * (numbers_of_events[0] - 1))
    elif event_number == 1:
        numbers_of_events[1] += 1
        existing_events.append("B" + '\'' * (numbers_of_events[1] - 1))
    elif event_number == 2:
        numbers_of_events[2] += 1
        existing_events.append("C" + '\'' * (numbers_of_events[2] - 1))
    elif event_number == 3:
        numbers_of_events[3] += 1
        existing_events.append("D" + '\'' * (numbers_of_events[3] - 1))
    elif event_number == 4:
        numbers_of_events[4] += 1
        existing_events.append("E" + '\'' * (numbers_of_events[4] - 1))


def get_restrictions(event1, event2, pivots, restriction_deviation):
    decreasing_deviation = random.randint(-restriction_deviation, 0)
    increasing_deviation = random.randint(0, restriction_deviation)
    num1 = get_event_number(event1)
    num2 = get_event_number(event2)
    diff = pivots[num2] - pivots[num1]
    return diff + decreasing_deviation, diff + increasing_deviation


def create_graphs(graphs_amount, events_amount, pivots, restriction_deviation):
    graphs = []

    graph_number = 0
    while graph_number < graphs_amount:
        existing_events = []
        numbers_of_events = [0, 0, 0, 0, 0]
        for j in range(events_amount):
            event_number = random.randint(0, 4)
            update_graph(event_number, existing_events, numbers_of_events)

        graph = {}
        for event in existing_events:
            graph[event] = []

        current_event = 0
        while current_event < events_amount:
            for j in range(0, current_event):
                if random.random() > 0.5:
                    if existing_events[current_event] not in graph[existing_events[j]]:
                        graph[existing_events[current_event]].append(existing_events[j])
            for j in range(current_event + 1, events_amount):
                if random.random() > 0.5:
                    if existing_events[current_event] not in graph[existing_events[j]]:
                        graph[existing_events[current_event]].append(existing_events[j])
            current_event += 1

        all_values = list(get_all_values(graph))
        flag = False
        for key in graph.keys():
            if key not in all_values and len(graph[key]) == 0:
                flag = True
                break
        if flag:
            continue
        graph_with_restrictions = []
        for key in graph.keys():
            for event in graph[key]:
                restriction1, restriction2 = get_restrictions(key, event, pivots, restriction_deviation)
                graph_with_restrictions.append([key, event, restriction1, restriction2])
        graphs.append(graph_with_restrictions)
        graph_number += 1
    return graphs


def evaluate_generation(generation):
    generation_fitness = [0] * len(generation)

    file = open('BD.txt')
    record_number = 1

    start_time = time.time()
    for record in file:
        print(record_number)
        for i in range(len(generation)):
            if is_record_satisfied(generation[i], record):
                generation_fitness[i] += 1
        record_number += 1
    total_time = time.time() - start_time
    print("Evaluation time: ", total_time)
    file.close()
    return generation_fitness, total_time


def select_best_parents(generation, fitness, num_parents):
    generation = copy.deepcopy(generation)
    fitness = fitness.copy()
    parents = []
    for i in range(num_parents):
        max_fitness_idx = fitness.index(max(fitness))
        parents.append(generation[max_fitness_idx])
        fitness[max_fitness_idx] = -999999
    return parents


def crossover(parents, num_children, c_prob):
    parents = copy.deepcopy(parents)
    children = []
    children_amount = 0
    i = 0
    while children_amount < num_children:
        x = random.random()
        if x > c_prob:
            i += 1
            continue
        parent1_index = i % len(parents)
        parent2_index = (i + 1) % len(parents)

        crossover_point1 = int(len(parents[parent1_index]) / 2)
        crossover_point2 = int(len(parents[parent2_index]) / 2)

        child1 = parents[parent1_index]
        child2 = parents[parent2_index]

        for gene_idx1, gene_idx2 in zip(range(crossover_point1), range(crossover_point2, len(child2))):
            child1[gene_idx1][2] = child2[gene_idx2][2]
            child1[gene_idx1][3] = child2[gene_idx2][3]
        for gene_idx1, gene_idx2 in zip(range(crossover_point2), range(crossover_point1, len(child1))):
            child2[gene_idx1][2] = child1[gene_idx2][2]
            child2[gene_idx1][3] = child1[gene_idx2][3]

        children.append(child1)
        if children_amount < num_children - 1:
            children.append(child2)
        children_amount += 2
        i += 1
    return children


def mutation(children, m_prob):
    mutants = copy.deepcopy(children)
    for mutant in mutants:
        random_value = random.random()
        if random_value > m_prob:
            continue
        random_idx = random.randint(0, len(mutant) - 1)
        mutant[random_idx][2] -= 1
        mutant[random_idx][3] += 1
    return mutants


def get_average_and_max_fitness_histories(fitness_history, num_generations):
    local_average = []
    local_maximum = []
    for history in fitness_history:
        local_average.append([np.mean(fitness) for fitness in history])
        local_maximum.append([np.max(fitness) for fitness in history])

    fitness_history_average = []
    for j in range(num_generations):
        average = 0
        for i in range(len(local_average)):
            average += local_average[i][j]
        fitness_history_average.append(average / len(local_average))

    fitness_history_max = []
    for j in range(num_generations):
        maximum = []
        for i in range(len(local_maximum)):
            maximum.append(local_maximum[i][j])
        fitness_history_max.append(max(maximum))
    return fitness_history_average, fitness_history_max


def optimize_elitism(generation, graphs_amount, num_generations, c_prob, m_prob):
    fitness_history = []
    evaluation_runtimes_history = []
    num_parents = int(graphs_amount / 2)
    num_children = graphs_amount - num_parents

    for i in range(num_generations):
        generation_fitness, evaluation_time = evaluate_generation(generation)
        fitness_history.append(generation_fitness)
        evaluation_runtimes_history.append(evaluation_time)

        parents = select_best_parents(generation, generation_fitness, num_parents)
        children = crossover(parents, num_children, c_prob)
        mutants = mutation(children, m_prob)

        for j in range(len(parents)):
            generation[j] = parents[j]
        for j in range(len(parents), len(mutants) + len(parents)):
            generation[j] = mutants[j - len(parents)]
        # generation = parents + mutants
    return fitness_history, evaluation_runtimes_history


def apply_elitism_n_times_same_generation(initial_generation, graphs_amount, num_generations, c_prob, m_prob, times):
    initial_generation_local_copy = copy.deepcopy(initial_generation)
    fitness_history = []
    evaluation_runtimes_history = []
    for i in range(times):
        print(i)
        initial_generation = copy.deepcopy(initial_generation_local_copy)
        fitness_history_local, evaluation_runtimes_history_local = optimize_elitism(initial_generation, graphs_amount,
                                                                                    num_generations, c_prob, m_prob)
        fitness_history.append(fitness_history_local)
        evaluation_runtimes_history.append(evaluation_runtimes_history_local)

    interesting_solutions = []
    for i in range(3):
        interesting_solutions.append(initial_generation[i])
    return get_average_and_max_fitness_histories(fitness_history,
                                                 num_generations), fitness_history, interesting_solutions, evaluation_runtimes_history


def apply_elitism_n_times_different_generations(graphs_amount, graphs_size, pivots, restrictions_deviation,
                                                num_generations, c_prob, m_prob,
                                                times):
    fitness_history = []
    evaluation_runtimes_history = []
    interesting_solutions = []
    for i in range(times):
        print(i)
        generation = create_graphs(graphs_amount, graphs_size, pivots, restrictions_deviation)
        fitness_history_local, evaluation_runtimes_history_local = optimize_elitism(generation, graphs_amount,
                                                                                    num_generations, c_prob, m_prob)
        fitness_history.append(fitness_history_local)
        evaluation_runtimes_history.append(evaluation_runtimes_history_local)
        interesting_solutions.append(generation[0])

    return get_average_and_max_fitness_histories(fitness_history,
                                                 num_generations), fitness_history, interesting_solutions, evaluation_runtimes_history


def main():
    pivots = find_pivots()

    c_prob = 0.1
    m_prob = 0.9

    graphs_amount = 10
    graphs_size = 6
    restrictions_deviation = 5
    num_generations = 5
    repetitions = 1
    initial_generation = create_graphs(graphs_amount, graphs_size, pivots, restrictions_deviation)

    # fitness_history_average_and_max, full_fitness_history, interesting_solutions, evaluation_runtimes_history = apply_elitism_n_times_same_generation(
    #     initial_generation,
    #     graphs_amount,
    #     num_generations, c_prob, m_prob,
    #     repetitions)
    fitness_history_average_and_max, full_fitness_history, interesting_solutions, evaluation_runtimes_history = apply_elitism_n_times_different_generations(
        graphs_amount, graphs_size, pivots, restrictions_deviation,
        num_generations, c_prob, m_prob,
        repetitions)

    print("Full history: ", full_fitness_history)
    print("Interesting solutions: ")
    for i in range(len(interesting_solutions)):
        last_try = full_fitness_history[len(full_fitness_history) - 1]
        print("Fitness: " + str(last_try[len(last_try) - 1][i]) + " Solution: " +
              str(interesting_solutions[i]))

    average_runtime = []
    for runtime_history in evaluation_runtimes_history:
        average_runtime.append(np.mean(runtime_history))
    average_runtime = np.mean(average_runtime)
    print("Average evaluation runtime: ", average_runtime)

    plt.plot(list(range(num_generations)), fitness_history_average_and_max[0], label='Average Fitness')
    plt.plot(list(range(num_generations)), fitness_history_average_and_max[1], label='Max Fitness')
    plt.legend()
    plt.title('Fitness through the generations')
    plt.xlabel('Generations')
    plt.ylabel('Fitness')
    plt.show()


if __name__ == "__main__":
    main()
