#!/usr/bin/env python3


import argparse
from gendiff.modules.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        )
    parser.add_argument('first_file')  # positional argument
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default="stylish",
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    format_ = args.format
    print(generate_diff(file1, file2, format_))


if __name__ == '__main__':
    main()
