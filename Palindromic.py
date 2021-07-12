"""
This program will loop through numbers 1 - 195 and
find palindromic numbers by adding a number to the same number backwards.
It will find the number(s) with the longest chain,
the largest possible number generated with this program,
the number of sequences that have a chain longer than 2 numbers, and length of the longest chain.
"""  
def backwards(n): # This function returns numbers backwards
    backwardsNum = str(n)[::-1]
    return int(backwardsNum)


def findLongestChain():
  """
This function loops finds the number with the longest list, the largest possible generated number, and the number of sequences with chains longer than 2. 
  """
  longestChain = -1  # Variable for the longest list of numbers
  largestNum = 0
  numList = []
  sequences = 0  # For Question 4, this is a variable for the # of sequences
  for n in range(1, 196):  # Loops through numbers from 1-195
      currentNum = n
      chainLength = 0
      while currentNum != backwards(currentNum):  # While the number is not palindromic
          currentNum += backwards(currentNum)  # Adds current number to the backwards number
          chainLength += 1  # Adds 1 to the length of the chain/list of numbers
          if currentNum > largestNum:  # Finds the largest number generated
              largestNum = currentNum
          if chainLength > 2:  # Records the # of sequences with chains longer than 2
              sequences += 1
          if chainLength > longestChain:  # Finds number(s) with the longest chain and puts it in numList
              longestChain = chainLength
              numList = [n]
          elif chainLength == longestChain: # If another number has the same chain length, add it to the numList
              numList.append(n)

  print(f"The number(s) with the longest chain: {numList}\n")
  print(f"The largest number generated from this program is {largestNum}\n")
  print(f"The number of sequences with chains longer than 2 is {sequences}\n")


def checkChain(n):  # This function finds the numbers in a chain
    chainList = [n] #Empty list for the numbers to go inside
    while n != backwards(n):
        n += backwards(n)
        chainList.append(n) #Adds number into chainList
    return chainList

print(__doc__)

findLongestChain()
print(f"The length of the longest chain is {len(checkChain(89))}\n") #Check the length of a number's chain by replacing the number here=
print(f"For proof of the longest chain, {checkChain(89)}") #Check what numbers are in a chain by replacing the number here