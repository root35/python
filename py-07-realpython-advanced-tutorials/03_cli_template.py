import argparse
import os
import sys


#-- Create the parser

my_parser = argparse.ArgumentParser(
    prog="myls",
    usage='%(prog)s [options] path',
    description='List the content of a folder.',
    epilog='Enjoy the program! :)',
    prefix_chars='-',
    allow_abbrev=False,
)


#-- Add the arguments

my_parser.add_argument('Path',
                       metavar='PATH',
                       type=str,
                       help='path to folder')

my_parser.add_argument('-l', '--long',
                       action='store_true',
                       help='enable long listing')

my_parser.add_argument('-c', action='store_const', const=42)
my_parser.add_argument('-o', action='store', nargs='?', default='value')
my_parser.add_argument('-a', action='store', nargs='*', default='44')
my_parser.add_argument('-r', action='store', nargs='+', choices=['head', 'tail'])
my_parser.add_argument('-z', action='store', nargs=argparse.REMAINDER)
my_parser.add_argument('-v', action='version')


#-- Execute the parse_args() method

args = my_parser.parse_args()


# Use the argument name 'Path'

input_path = args.Path

if not os.path.isdir(input_path):
    print(f'Specified path does not exist: {input_path}')
    sys.exit()

for line in os.listdir(input_path):
    if args.long:
        size = os.stat(os.path.join(input_path, line)).st_size
        line = f'{size}  {line}'
    print(line)
