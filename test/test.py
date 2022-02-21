from random import randint
from calendar import month


def output(code: int) -> None:
    match code:
        case 0:
            print("hello everyone")
        case 1:
            print(f"current month:\n{month(2022, 2)}")
        case _:
            print("invalid code, pls repeat")
            output(randint(0, 2))


def main():
    output(randint(0, 2))


if __name__ == "__main__":
    main()
