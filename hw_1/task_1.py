import sys

def number_lines(file):
    for i, line in enumerate(file, start=1):
        print(f"{i}\t{line}", end="")

def main():
    if len(sys.argv) <= 1:
        number_lines(sys.stdin)
        return
    filename = sys.argv[1]
    try:
        with open(filename, "r", encoding="utf-8") as file:
            number_lines(file)
    except FileNotFoundError:
        print(f"nl(python script): {filename}: No such file or directory", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
