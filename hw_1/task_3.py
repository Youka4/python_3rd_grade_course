import sys
import os


def count_file_stats(file):
    lines = 0
    words = 0
    bytes_count = 0

    for line in file:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode("utf-8"))

    return lines, words, bytes_count


def print_stats(lines, words, bytes_count, filename=""):
    print(f"{lines}\t{words}\t{bytes_count}\t{filename}")


def main():
    args = sys.argv[1:]
    total_lines, total_words, total_bytes = 0, 0, 0

    if not args:
        lines, words, bytes_count = count_file_stats(sys.stdin)
        print_stats(lines, words, bytes_count)
        return

    for filename in args:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                lines, words, _ = count_file_stats(file)
            bytes_count = os.stat(filename).st_size
            print_stats(lines, words, bytes_count, filename)

            total_lines += lines
            total_words += words
            total_bytes += bytes_count
        except FileNotFoundError:
            print(f"wc(python script): {filename}: No such file or directory", file=sys.stderr)

    if len(args) > 1:
        print_stats(total_lines, total_words, total_bytes, "total")


if __name__ == "__main__":
    main()
