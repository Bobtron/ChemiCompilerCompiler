import os.path
import sys
import math


def get_tx_ax(tmp):
    return [0, tmp - 273] if tmp > 273 else [273 - tmp, 0]


def mov_ptr(target, ptr, arr):
    mov = 0
    while target != arr[ptr]:
        if target < arr[ptr]:
            mov -= 1
            ptr -= 1
        else:
            mov += 1
            ptr += 1
    return ">" * mov if mov > 0 else "<" * -mov, ptr


if __name__ == "__main__":
    filename = ""

    while True:
        print("Enter the filename:")
        filename = input()
        if os.path.isfile(filename):
            break
        print("Not a file, try again")

    commands = []

    reg_ops = ['}', ')', "'"]
    main_ops = {
        'MOVE': '@',
        'TEMP': "$",
        'ISOLATE': '#'
    }

    all_ints = set()

    with open(filename, 'r') as file:
        for line in file.readlines():
            commands.append(line[:-1].split())

    # print(commands)

    for i in range(len(commands)):
        if commands[i][0] == 'TEMP':
            tmp = int(commands[i].pop())
            commands[i].extend(get_tx_ax(tmp))
        commands[i].append(commands[i].pop(0))
        for j in range(len(commands[i]) - 1):
            commands[i][j] = int(commands[i][j])
            all_ints.add(commands[i][j])

    all_ints = sorted(list(all_ints))

    # print(commands)
    # print(all_ints)

    ptr = len(all_ints) - 1
    init_str = ">".join(["+" * i for i in all_ints])
    regs = [-1, -1, -1]

    # print(ptr)
    # print(init_str)

    all_beakers = [[0] for i in range(10)]
    # print(all_beakers)

    chem_fuck_program = [init_str]

    for command in commands:
        string = ""
        for i in range(len(command) - 1):
            # if the register has already been set to the desired value
            if i < len(reg_ops) and regs[i] == command[i]:
                continue
            # Shift the ptr, then set the register
            shift, ptr = mov_ptr(command[i], ptr, all_ints)
            string += shift
            if i < len(reg_ops):
                regs[i] = command[i]
                string += reg_ops[i]
        string += main_ops[command[-1]]
        if command[-1] == 'MOVE' and command[1] <= 10:
            all_beakers[command[0] - 1][0] += command[2]
            all_beakers[command[1] - 1][0] -= command[2]
            if len(all_beakers[command[0] - 1]) > 1:
                print("MOVE from beaker " + str(command[0]) + " with multiple reagents")
        elif command[-1] == 'ISOLATE' and command[1] <= 10:
            all_beakers[command[1] - 1][0] -= command[2]
            while len(all_beakers[command[0] - 1]) < command[3]:
                all_beakers[command[0] - 1].append(0)
            all_beakers[command[0] - 1][command[3] - 1] += command[2]

        chem_fuck_program.append(string)
    chem_fuck_program.append("~")

    for line in chem_fuck_program:
        print(line)

    # print(all_beakers)

    i = len(all_beakers) - 1
    while i >= 0:
        if sum(all_beakers[i]) <= 0:
            all_beakers.pop(i)
        i -= 1

    min_reps = sys.maxsize

    for beaker in all_beakers:
        if 100 / sum(beaker) < min_reps:
            min_reps = math.floor(100 / sum(beaker))

    print("\nCan make recipe " + str(min_reps) + " times.")

    for i in range(len(all_beakers)):
        # string = "Beaker " + str(i + 1) + ": "
        beaker_size = 50 if sum(all_beakers[i]) * min_reps <= 50 else 100
        once_str = "("
        total_str = ""
        for reagent in all_beakers[i]:
            once_str += str(reagent) + "+"
            total_str += str(reagent * min_reps) + "+"
        once_str = once_str[:-1] + ")"
        total_str = total_str[:-1]
        string = once_str + " " + total_str + "/" + str(beaker_size)
        print(string)

    # print(min_reps)
#




