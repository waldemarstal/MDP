#-*- coding: utf-8 -*-
import sys
from pylab import *
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
        xlabel('Number of iterations')
        ylabel('Utility estimates')
        title('Graph of utility')
        axis([0, 25, 0, 1])
        data = open(file_name, 'r')
        data_of_usability = open('data_of_usability.txt', 'w')
        data_of_politics = open('data_of_politics.txt', 'w')
        lines = data.readlines()
        param = lines[0].split()
        for line in lines[1:]:
            world.append([l.split(':') for l in line.split()])
        obj = ValueIterateAlgorithm(
            param[0], param[1], world, param[2], param[3], param[4], param[5])
        for i in range(20):
            obj.usability_table()
            data_of_usability.write(obj.str_repr_us_tab())
            data_of_usability.write('\n')
        obj.politics_table()
        data_of_politics.write(obj.str_repr_pol_tab())
        data.close()
        data_of_usability.close()
        data_of_politics.close()
        for key, value in obj.dict_with_column.iteritems():
            plot(value, label=key)
        legend()
        savefig('graph.png')


    except Exception as e:
        print '%s!' % e

if __name__ == '__main__':
    main()