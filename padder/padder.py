#!/usr/bin/python
import argparse

def main():
    parser = argparse.ArgumentParser(description='Padding file with zeroes')
    parser.add_argument('filenames', metavar='filename', type=str, nargs='+',
                   help='filenames')
    parser.add_argument('-s', dest='size',default='1M',
                   help='target size in K or M')

    args = parser.parse_args()
    print args

if __name__ == "__main__":
    main()
