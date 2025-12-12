from itertools import combinations_with_replacement


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
            lights_start = 1
            lights_end = machine_str.rindex("]")
            buttons_start = machine_str.index("(")
            buttons_end = machine_str.rindex(")") + 1
            joltage_reqs_start = machine_str.index("{") + 1
            joltage_reqs_end = machine_str.index("}")
            lights = list(machine_str[lights_start:lights_end])
            buttons = [list(map(int, button[1:-1].split(","))) for button in
                       machine_str[buttons_start:buttons_end].split()]
            joltage_reqs = list(map(int, machine_str[joltage_reqs_start:joltage_reqs_end].split(",")))
            machines.append((lights, buttons, joltage_reqs))
        f.close()

    for machine in machines:
        current_lights = []
        correct_lights, buttons, joltage_reqs = machine
        num_button_presses = 0
        while current_lights != correct_lights:
            num_button_presses += 1
            for button_combo in combinations_with_replacement(buttons, num_button_presses):
                current_lights = ['.'] * len(correct_lights)
                for button in button_combo:
                    for light in button:
                        current_lights[light] = switch_light(current_lights[light])
                if current_lights == correct_lights:
                    break
        total_button_presses += num_button_presses

    print(total_button_presses)


if __name__ == "__main__":
    main()
