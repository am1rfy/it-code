from calendar import month
from prettytable import PrettyTable


def output(code: int) -> None:
    match code:
        case 0:
            print("hello everyone")
        case 1:
            print(f"current month:\n{month(2022, 2)}")
        case 2:
            mytable = PrettyTable()

            mytable.field_names = ["some_field1", "some_field2", "some_field3"]

            mytable.add_row(["some_field1", 1, 2])
            mytable.add_row(["some_field1", 1, 2])
            mytable.add_row(["some_field1", 1, 2])

            print(mytable)
        case _:
            print("invalid code, pls repeat")
            output(input())


def main():
    output(int(input()))


if __name__ == "__main__":
    main()
