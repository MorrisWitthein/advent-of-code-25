import argparse
import part_one.solve as part_one
import part_two.solve as part_two


def load_input(input_file_path):
    input_data = ""
    with open(input_file_path, "r") as file:
        input_data = file.read().strip()
    return input_data


def main():
    parser = argparse.ArgumentParser(
        description="Run parts of the Advent of Code project"
    )
    parser.add_argument(
        "-p",
        "--part",
        default=1,
        type=int,
        choices=[1, 2],
        help="Which part to run (1 or 2)",
    )
    parser.add_argument("-i", "--input-file-path", type=str, help="Path to input file")

    args = parser.parse_args()

    input_file_path = "inputs/input"
    if args.input_file_path:
        input_file_path = f"inputs/{args.input_file_path}"
    if args.part == 2:
        print("Running Part Two")
        part_two.solve(load_input(input_file_path))
    else:
        print("Running Part One")
        part_one.solve(load_input(input_file_path))


if __name__ == "__main__":
    main()
