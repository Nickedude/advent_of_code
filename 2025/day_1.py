from typing import NamedTuple


class Instruction(NamedTuple):

    direction: str
    num_steps: int


def solve_snd(instructions: list[Instruction]):
    size = 100
    current = 50
    num_at_zero = 0
    
    for i in instructions:
        if i.direction == "L":
            predecessor = current - i.num_steps
            distance = current
        elif i.direction == "R":
            predecessor = current + i.num_steps
            distance = size - current
        else:
            raise ValueError(f"Unknown direction: {i.direction}")

        steps_left = i.num_steps 
        steps_left = steps_left - distance

        if distance > 0 and steps_left >= 0:
            num_at_zero += 1

        while steps_left >= size:
            steps_left -= size
            num_at_zero += 1

        current = (predecessor % size)

        if steps_left > 0 and current == 0:
            num_at_zero += 1

    return num_at_zero


def solve_fst(instructions: list[Instruction]):
    size = 100
    current = 50
    num_at_zero = 0
    
    for i in instructions:
        if i.direction == "L":
            predecessor = current - i.num_steps
        elif i.direction == "R":
            predecessor = current + i.num_steps
        else:
            raise ValueError(f"Unknown direction: {i.direction}")

        current = (predecessor % size)

        if current == 0:
            num_at_zero += 1

    return num_at_zero


def read():
    instructions = []
    with open("input.txt") as file:
        for line in file.readlines():
            instructions.append(
                Instruction(
                    direction=line[0],
                    num_steps = int(line[1:])
                )
            )

    return instructions

def main():
    instructions = read()
    answer = solve_fst(instructions)
    print(answer)
    answer = solve_snd(instructions)
    print(answer)


if __name__ == "__main__":
    main()
