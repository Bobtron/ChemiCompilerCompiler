import os.path


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
    filename = "input_cmds.txt"

    # while True:
    #     print("Enter the filename:")
    #     filename = input()
    #     if os.path.isfile(filename):
    #         break
    #     print("Not a file, try again")

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

    print(commands)

    for i in range(len(commands)):
        if commands[i][0] == 'TEMP':
            tmp = int(commands[i].pop())
            commands[i].extend(get_tx_ax(tmp))
        commands[i].append(commands[i].pop(0))
        for j in range(len(commands[i]) - 1):
            commands[i][j] = int(commands[i][j])
            all_ints.add(commands[i][j])

    all_ints = sorted(list(all_ints))

    print(commands)
    print(all_ints)

    ptr = len(all_ints) - 1
    init_str = ">".join(["+" * i for i in all_ints])
    regs = [-1, -1, -1]

    print(ptr)
    print(init_str)

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
        print(string)
    print("~")




