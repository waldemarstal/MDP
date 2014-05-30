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
        world = []
        data = open(file_name, 'r')
        result = open('result.txt', 'w')
        lines = data.readlines()
        param = lines[0].split()
        for line in lines[1:]:
            world.append([l.split(':') for l in line.split()])
        obj = ValueIterateAlgorithm(
            param[0], param[1], world, param[2], param[3], param[4], param[5])
        for i in range(20):
            obj.usability_table()
            result.write(obj.str_repr_us_tab())
            result.write('\n')
        data.close()
        result.close()

    except Exception as e:
        print '%s!' % e

if __name__ == '__main__':
    main()