def sum_total_difference(list_one, list_two):
    list_one_sorted = sorted(list_one)
    list_two_sorted = sorted(list_two)

    values = zip(list_one_sorted, list_two_sorted)

    difference_values = []
    for i in values:
        difference_values.append(abs(i[0] - i[1]))

    return sum(difference_values)


def parse_input(filename):
    with open(filename, "r") as input:
        location_IDs = input.readlines()

    list_one = []
    list_two = []
    for line in location_IDs:
        line = line.split()
        list_one.append(int(line[0]))
        list_two.append(int(line[1]))

    return list_one, list_two


def main():
    list_one, list_two = parse_input("dayone_input")
    total = sum_total_difference(list_one, list_two)
    print(total)


if __name__ == "__main__":
    main()
