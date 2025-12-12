from itertools import combinations_with_replacement, chain
from pulp import *


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
        buttons, joltage_reqs = machine
        # Step 1: Creating the minimisation problem
        model = pulp.LpProblem("Minimise_Button_Presses", LpMinimize)
        # Step 2: Creating decision variables
        # x[i] represents "how many times should we press button i?"
        x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(len(buttons))]
        # Step 3: Setting the objective function
        # Minimising the total number of button presses
        model += pulp.lpSum(x)
        # Step 4: Adding constraints
        # One per joltage counter
        for counter_idx in range(len(joltage_reqs)):
            # Building the left side of the equation: sum of all buttons that affect this counter
            constraint = pulp.lpSum([x[button_idx] for button_idx in range(len(buttons))
                                     if counter_idx in buttons[button_idx]])
            # Adding the constraint: the sum must equal the target joltage
            # This creates equations like: x[1] + x[3] + x[5] = 41
            model += constraint == joltage_reqs[counter_idx]
        model.solve()
        button_presses = sum(pulp.value(var) for var in x)
        total_button_presses += button_presses

    print(total_button_presses)


if __name__ == "__main__":
    main()
