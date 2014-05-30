#-*- coding: utf-8 -*-
import sys
from optparse import OptionParser
parser = OptionParser()
(options, args) = parser.parse_args()
from main import ValueIterateAlgorithm


def main():
    if len(args) != 1:
        print 'Incorrect number of arguments! Try again.'
        sys.exit(0)
    file_name = args[0]
    try:
        data = open(file_name, 'r')
        result = open('result.txt', 'w')
        data.readlines()
        world = [
            ['*', '*', '*', '1'],
            ['*', '.', '*', '-1'],
            ['*', '*', '*', '*'],
        ]
        obj = ValueIterateAlgorithm(
            4, 3, world, 0.99, (0, 0), 0.1, 0.8)
        for i in range(20):
            obj.usability_table()
            result.write(str(obj.u))
            result.write('\n')
        data.close()
        result.close()

    except Exception as e:
        print '%s!' % e


if __name__ == '__main__':
    main()