import csv
from itertools import combinations, chain
from functools import partial
import math


def calc_distance(pair):
    b1, b2 = pair
    return math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2)


def sort_by_distance(pair):
    return pair[2]


def filter_first_box_circuits(circuit, pair):
    return pair[0] in circuit and pair[1] not in circuit


def filter_second_box_circuits(circuit, pair):
    return pair[0] not in circuit and pair[1] in circuit


def filter_both_boxes_circuits(circuit, pair):
    return pair[0] in circuit and pair[1] in circuit


def main():
    with open('day8_input.csv', 'r') as f:
        f_reader = csv.reader(f)
        j_boxes = [tuple(map(int, row)) for row in f_reader]
        f.close()

    pairs = combinations(j_boxes, 2)
    pairs_distances = [pair + (calc_distance(pair),) for pair in pairs]
    pairs_distances.sort(key=sort_by_distance)

    circuits = [list(pairs_distances[0][:2])]
    connection_count = 1

    for pair in pairs_distances[1:]:
        c_circuits = circuits.copy()
        first_only = list(filter(partial(filter_first_box_circuits, pair=pair), c_circuits))
        second_only = list(filter(partial(filter_second_box_circuits, pair=pair), c_circuits))
        both = list(filter(partial(filter_both_boxes_circuits, pair=pair), c_circuits))
        if first_only and second_only:
            circuit = first_only[0] + second_only[0]
            circuits.remove(first_only[0])
            circuits.remove(second_only[0])
            circuits.append(circuit)
        elif first_only:
            circuit = first_only[0]
            circuit.append(pair[1])
        elif second_only:
            circuit = second_only[0]
            circuit.append(pair[0])
        elif not first_only and not second_only and not both:
            circuits.append([pair[0], pair[1]])
        connection_count += 1
        sorted_circuit_sizes = sorted([len(circuit) for circuit in circuits], reverse=True)
        if len(circuits[0]) == len(j_boxes):
            print(pair)
            print(pair[0][0]*pair[1][0])
            break


if __name__ == "__main__":
    main()