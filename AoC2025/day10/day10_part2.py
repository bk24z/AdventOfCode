from itertools import combinations_with_replacement, chain


def switch_light(light):
    if light == '.':
        return '#'
    return '.'


def main():
    total_button_presses = 0
    machines = []
    with open("day10_input.txt") as f:
        machine_strs = f.read().splitlines()
        for machine_str in machine_strs:
            buttons_start = machine_str.index("(")
            buttons_end = machine_str.rindex(")") + 1
            joltage_reqs_start = machine_str.index("{") + 1
            joltage_reqs_end = machine_str.index("}")
            buttons = [list(map(int, button[1:-1].split(","))) for button in
                       machine_str[buttons_start:buttons_end].split()]
            joltage_reqs = list(map(int, machine_str[joltage_reqs_start:joltage_reqs_end].split(",")))
            machines.append((buttons, joltage_reqs))
        f.close()

    for machine in machines:
        current_joltages = []
        buttons, joltage_reqs = machine
        print(max(list(chain(*buttons))))
        num_button_presses = int(max(joltage_reqs) / max(list(chain(*buttons))))
        while current_joltages != joltage_reqs:
            num_button_presses += 1
            print(num_button_presses)
            for button_combo in combinations_with_replacement(buttons, num_button_presses):
                current_joltages = [0] * len(joltage_reqs)
                for button in button_combo:
                    for light in button:
                        current_joltages[light] += 1
                if current_joltages == joltage_reqs:
                    print(num_button_presses,button_combo,current_joltages)
                    break
        total_button_presses += num_button_presses

    print(total_button_presses)


if __name__ == "__main__":
    main()
