#!/usr/bin/python3

import sys, getopt, string
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

def index(r,c,v,N):
   return ((r-1)*(N**2) + ((c-1)*N) + v)


def c1(instance,N,totals):

  #condition 1 ( At least 1 number in a cell):
    
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      c1 = "" # reset string after loop ends
      for k in range(1, N + 1):
        c1 += "{0} ".format(index(i, j, k, N))
          
      c1 += "0"
      totals.append(c1)


def c2(instance,N,totals):
  #condition 2 ( At most 1 number in a cell):
    for r in range (1,N+1):
       for c in range(1,N+1):
          for vr in range(1,N+1):
             for vc in range (vr +1, N+1):
                c2 = str(-(index(r,c,vr,N))) + ' ' + str(-(index(r,c,vc, N))) + ' '
                totals.append(c2)
                c2 += '0'


def c3(instance, N, totals):
  #constraint 3:
    for r in range (1,N+1):
      for k in range(1,N+1):
         for c in range(1,N):
            for v in range (c+1,N+1):
               c3 = str(-(index(r,c,k,N))) + ' ' + str(-(index(r,v,k,N))) + ' '
               totals.append(c3)
               c3 += '0'


#conditon 4 (No row contains duplicate numbers):
def c4(instance, N, totals):

  for c in range (1,N+1):
    for k in range(1,N+1):
       for r in range(1,N):
          for v in range (r+1,N+1):
            c4 = str(-(index(r,c,k,N))) + ' ' + str(-(index(v,r,k,N))) + ' '
            totals.append(c4)
            c4 += '0'





def c5(instance, N, totals):
#condition 5:
  for r in range(1,N+1):
     for c in range(1,N+1):
        v = instance[r-1][c-1]
        if v != 0 :
           c5 = str(index(r,c,v,N)) + ' ' 
          
           totals.append(c5)
           c5 += '0'
""" Question 1 """


def toCNF (N, instance, outputfile):
    """ Constructs the CNF formula C in Dimacs format from a sudoku grid."""
    """ OUTPUT: Write Dimacs CNF to output_file """
    output_file = open(outputfile, "w")
    "*** YOUR CODE HERE ***"
    varnum = N*N*N
    #output_file.write('p cnf %d %d\n' % (varnum,N))

    totals = []

          
    c1(instance, N, totals)

    c2(instance,N, totals)

    c3(instance,N, totals)

    c4(instance,N, totals)
    
    c5(instance,N, totals)


    num = len(totals) 

    output_file.write("p cnf {0} {1}\n".format(varnum, num))

    #used to write into the file
    for counter in range(len(totals)):
         output_file.write("{0}\n".format(totals[counter]))
    
    "*** YOUR CODE ENDS HERE ***"
    output_file.close()




if __name__ == "__main__":
   main(sys.argv[1:])
