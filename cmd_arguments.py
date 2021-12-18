# Handle command line arguments in Python

# sys module is used to handle Python runtime environment. 
# We can use it to handle command line arguments as well

import sys
# print all
print ("All arguments :"+ str(sys.argv))

# print first :: this is the script name
print ("First argument :"+sys.argv[0])

# print third
print ("Third argument :"+sys.argv[2])

#python cmd_arguments.py 1 def xyz 100
#Output
#All arguments :['cmd_arguments.py', '1', 'def', 'xyz', '100']
#First argument :cmd_arguments.py
#Third argument :def
