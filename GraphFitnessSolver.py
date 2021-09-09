from Test import evaluate_generation


def test_graph(graph):
    return evaluate_generation(graph)


def main():
    # graph = [['C', "C'", -2, 0], ["C'", 'D', -3, 4], ["C'", "C''", -3, 0], ["C''", 'D', -1, 3], ["C''", 'C', 0, 4]]
    graph = [
        [['A', 'B', -5, 10], ['A', 'C', -5, 22], ['B', 'C', -2, 21]]]
    fitness = test_graph(graph)
    print(fitness)


if __name__ == "__main__":
    main()
