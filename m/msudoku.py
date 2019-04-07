#!/usr/bin/python3

import sys, getopt
#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
# num_hours_i_spent_on_this_assignment = 0
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
# <Your feedback goes here>
"""

"""
#####################################################
#####################################################

def main(argv):
   inputfile = ''
   N=0
   try:
      opts, args = getopt.getopt(argv,"hn:i:",["N=","ifile="])
   except getopt.GetoptError:
      print ('sudoku.py -n <size of Sodoku> -i <inputputfile>')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('sudoku.py  -n <size of Sodoku> -i <inputputfile>')
           sys.exit()
       elif opt in ("-n", "--N"):
           N = int(arg)
       elif opt in ("-i", "--ifile"):
           inputfile = arg
   instance = readInstance(N, inputfile)
   toCNF(N,instance,inputfile+str(N)+".cnf")




def readInstance (N, inputfile):
    if inputfile == '':
        return [[0 for j in range(N)] for i in range(N)]
    with open(inputfile, "r") as input_file:
        instance =[]
        for line in input_file:
            number_strings = line.split() # Split the line on runs of whitespace
            numbers = [int(n) for n in number_strings] # Convert to integers
            if len(numbers) == N:
                instance.append(numbers) # Add the "row" to your list.
            else:
                print("Invalid Sudoku instance!")
                sys.exit(3)
        return instance # a 2d list: [[1, 3, 4], [5, 5, 6]]

def index(i, j, k):
    return 81 * (i - 1) + 9 * (j - 1) + k
    #return (i - 1) * (3 ** 2) + (j - 1) * 3 + (k - 1) + 1

""" Question 1 """
def toCNF (N, instance, outputfile):
    """ Constructs the CNF formula C in Dimacs format from a sudoku grid."""
    """ OUTPUT: Write Dimacs CNF to output_file
        the number N => NxN
        an instance of sudoku of size NxN
        and a string (for the name of output file).
    """
    output_file = open(outputfile, "w")

    "*** YOUR CODE HERE ***"
    rows = N
    columns = N
    values = range(1, rows+1)
    cells = len(values) * N
    variables = N*N*N
    res = []
    
    # Each cell contains at least one copy of any number.
    for i in range(1, rows + 1):
        for j in range(1, N + 1):
            c1 = "" # reset string after loop ends
            for k in range(1, columns + 1):
                c1 += "{0} ".format(index(i, j, k,N))
            c1 += "0"
            res.append(c1)
    
    # Each cell contains at most one copy of any number.
    for i in range(1, rows + 1):
        for j in range(1, N + 1):
            for vi in range(1, N+1):
                for vj in range(vi + 1, N+1):
                    c2 = "-{0} ".format(index(i, j, vi))
                    c2 += "-{0} 0".format(index(i, j, vj))
                    res.append(c2)
    
    # No two fields in any column contain the same value.
    for i in range(1, rows + 1):
        for k in range(1, N + 1):
            for j in range(1, columns):
                for val in range(j + 1, N + 1):
                    c3 = "{0} {1} 0".format(-index(i, j, k), -index(i, val, k))
                    res.append(c3)
    
    # No two fields in any row contain the same value
    for j in range(1, rows + 1):
        for k in range(1, N + 1):
            for i in range(1, columns):
                for val in range(i + 1, N + 1):
                    c4 = "{0} {1} 0".format(-index(i, j, k), -index(val, j, k))
                    res.append(c4)
    
    # restrict cells that were labeled in the puzzle grid to keep that label
    for i in range(1, N+1):
        for j in range(1, N+1):
            value = instance[i - 1][j - 1]
            if value !=  0: # i am not sure about this loop set, get values already in the board
                c5 = "{0} 0".format(index(i, j, value))
                res.append(c5)
    
    # cnf format and output to file
    clauses = len(res)
    output_file.write("p cnf {0} {1}\n".format(variables, clauses))
    for i in range(len(res)):
	       output_file.write("{0}\n".format(res[i]))

    "*** YOUR CODE ENDS HERE ***"
    output_file.close()


if __name__ == "__main__":
   main(sys.argv[1:])
