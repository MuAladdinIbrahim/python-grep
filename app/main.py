import sys
import re

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    print(type(pattern), len(pattern))
    if(len(pattern) > 2):
        return positive_group(input_line, pattern)
    if(pattern == "\d"):
        return contains_number(input_line)
    if(pattern == "\w"):
        return contains_alphanumeric(input_line)
    if len(pattern) == 1:
        return pattern in input_line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")

def positive_group(input_line, pattern):
    return input_line in pattern

def contains_number(input_line):
    return re.search('\d', input_line)

def contains_alphanumeric(input_line):
    return input_line.isalnum()

def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
