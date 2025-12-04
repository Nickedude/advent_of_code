from typing import NamedTuple

class IdRange(NamedTuple):

    start: int
    stop: int


def parse() -> list[IdRange]:
    with open("input.txt") as file:
        results = []

        line = file.readline()
        line = line.strip("\n")
        ranges = line.split(",")

        for r in ranges:
            start, stop = r.split("-")
            results.append(IdRange(int(start),int(stop)))

        return results


def solve_fst(ranges: list[IdRange]) -> int:
    invalid = []

    for r in ranges:
        for i in range(r.start, r.stop + 1):
            num_str = str(i)

            if not (len(num_str) % 2 == 0):
                continue

            half_length = len(num_str) // 2
            fst = int(num_str[:half_length])
            snd = int(num_str[half_length:])

            if fst == snd:
                invalid.append(i)

    return sum(invalid)


def solve_snd(ranges: list[IdRange]) -> int:
    invalid = []

    for r in ranges:
        for i in range(r.start, r.stop + 1):
            num_str = str(i)

            if len(num_str) <= 1:
                continue

            half_length = len(num_str) // 2

            for j in range(1,half_length+1):
                fst = int(num_str[:j])
                correct = True
                for k in range(j, len(num_str), j):
                    snd = int(num_str[k:k+j])

                    if snd != fst:
                        correct = False
                        break

                if correct:
                    invalid.append(i)
                    break

    return sum(invalid)


def main():
    ranges = parse()
    print(solve_fst(ranges))
    print(solve_snd(ranges))


if __name__ == "__main__":
    main()
