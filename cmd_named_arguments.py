# Handle command line arguments in Python

# argparse module is used to handle named arguments

import argparse

parser=argparse.ArgumentParser()

parser.add_argument('--id', help='ID argument')
parser.add_argument('--city', help='CITY argument')
args=parser.parse_args()

# print ID
print ("ID value is :"+ str(args.id))
# print CITY
print ("CITY value is :"+ str(args.city))

#python cmd_named_arguments.py --id=1 --city=Paris
#Output
#ID value is :1
#CITY value is :Paris