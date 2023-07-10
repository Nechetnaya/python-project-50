#!/usr/bin/env python3


import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        )
    parser.add_argument('first_file')  # positional argument
    parser.add_argument('second_file')
    args = parser.parse_args(['-h'])

