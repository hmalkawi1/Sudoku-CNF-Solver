#!/usr/bin/python3

import sys, getopt

class SatInstance:
    def __init__(self):
        pass
    def from_file(self, inputfile):
        self.clauses = list()
        self.VARS = set()
        self.p = 0
        self.cnf = 0
        with open(inputfile, "r") as input_file:
            self.clauses.append(list())
            maxvar = 0
            for line in input_file:
                tokens = line.split()
                if len(tokens) != 0 and tokens[0] not in ("p", "c"):
                    for tok in tokens:
                        lit = int(tok)
                        maxvar = max(maxvar, abs(lit))
                        if lit == 0:
                            self.clauses.append(list())
                        else:
                            self.clauses[-1].append(lit)
                if tokens[0] == "p":
                    self.p = int(tokens[2])
                    self.cnf = int(tokens[3])
            assert len(self.clauses[-1]) == 0
            self.clauses.pop()
            if not (maxvar == self.p):
                print("Non-standard CNF encoding!")
                sys.exit(5)
      # Variables are numbered from 1 to p
        for i in range(1,self.p+1):
            self.VARS.add(i)
    def __str__(self):
        s = ""
        for clause in self.clauses:
            s += str(clause)
            s += "\n"
        return s



def main(argv):
   inputfile = ''
   verbosity=False
   inputflag=False
   try:
      opts, args = getopt.getopt(argv,"hi:v",["ifile="])
   except getopt.GetoptError:
      print ('DPLLsat.py -i <inputCNFfile> [-v] ')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
           print ('DPLLsat.py -i <inputCNFfile> [-v]')
           sys.exit()
    ##-v sets the verbosity of informational output
    ## (set to true for output veriable assignments, defaults to false)
       elif opt == '-v':
           verbosity = True
       elif opt in ("-i", "--ifile"):
           inputfile = arg
           inputflag = True
   if inputflag:
       instance = SatInstance()
       instance.from_file(inputfile)
       solve_dpll(instance, verbosity)
   else:
       print("You must have an input file!")
       print ('DPLLsat.py -i <inputCNFfile> [-v]')


""" Question 2 """
# Finds a satisfying assignment to a SAT instance,
# using the DPLL algorithm.
# Input: a SAT instance and verbosity flag
# Output: print "UNSAT" or
#    "SAT"
#    list of true literals (if verbosity == True)
#    list of false literals (if verbosity == True)
#
#  You will need to define your own
#  solve(VARS, F), pure-elim(F), propagate-units(F), and
#  any other auxiliary functions


#def Startvar(instance):
    #counter = {}
    #for clauses in instance.clauses:
        

#checks if clause is unit clause

def unitprop(F):
    units= set()
    
    for clause in instance.clauses :
       if len(clause) == 1 :
           units.add(clause[0])

    for unit in units:
        for i in instance.clauses[:]:
            if(unit*-1) in i:
                i.remove((unit*-1))
            if unit in i and len(i) > 1:
                instance.clauses.remove(i)
            
    return units
        



# Pure Elimination : Pure Clauses can be removed
# Just set the pure literals to true
def pureEliminate(clauses):
  
    dictionary = {}
    for i in (instance.VARS):
      dictionary[i] = ["0"]

    for i in dictionary[i]:
      for clause in clauses :
        for v in range (len(clauses)):
          if i == (clauses[clause][v]):
            dictionary [i] = [dictionary[i] + 1]


    return dictionary
      
        





def solve_dpll(instance, verbosity):
    #print(instance)
    #print(instance.VARS)
    #print(verbosity)
    ###########################################
    # Start your code
    #print(len(instance.clauses))
    #proplist = unitprop(instance)

    #varnum= pureEliminate(instance)
    mydic = pureEliminate(instance.clauses)
    print(mydic)
    
    #print (proplist)
    #print(varnum)
    return True
    ###########################################


if __name__ == "__main__":
   main(sys.argv[1:])
