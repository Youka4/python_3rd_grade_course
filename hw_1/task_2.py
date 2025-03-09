import sys

def tail(file, num_lines=10):
    lines = file.readlines()[-num_lines:]
    for line in lines:
        print(line, end="")

def main():
    args = sys.argv[1:]
    if not args:
        tail(sys.stdin, num_lines=17)
        return
    is_multiple_files = len(args) > 1
    for i, filename in enumerate(args):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                if is_multiple_files:
                    if i > 0:
                        print()
                    print(f"==> {filename} <==")
                tail(file)
        except FileNotFoundError:
            print(f"tail(python script): cannot open {filename} for reading: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    main()
