"""
This program excecutes the collatz conjecture.
It loops through 2-1000 and counts the number of non-ending cycles or infinite cycles,
finds the length of the longest series until needing to loop,
and finds the number that creates the longest series.
"""

def isInfinite(num):  # Returns true or false if chain is infinite
    """
    This function checks if a number produces an infinite chain or not.
    """
    
    numList = [] # Store numbers in chain
    
    while num != 1:
        numList.append(int(num)) # Add number to chain before each iteration

        if num % 2 == 0: # Even
            num /= 2
            
        else: # Odd
          num = (3 * num) - 1

        if num in numList: # Check loop. If true, return true and length of chain
            return True, numList
        
    return False, None # Non-infinite loop, return false and None, just so that there's something to unpack


def solve():
    """
    This function uses the isInfinite() function to find infinite cycles and longest chains, solving the problems.
    """

    infiniteCycles = 0 # Count infinite cycles
    currentMaxChain = [] # Stores the largest chain (at any point in loop)

    for n in range(2, 1001): # Loop through 2 - 1000
    
        # If doesLoop, the actual chain is returned as well.
        doesLoop, chain = isInfinite(n)

        if doesLoop:
            infiniteCycles += 1 # Count cycle

            # Check if the chain we have now is longer than the previous longest chain. If so, we've found a new longest chain!
            if len(chain) > len(currentMaxChain): 
                currentMaxChain = chain
            
    # Return the (1) # of infinite cycles, (2) the length of max chain and (3) the starting number of the max chain
    return infiniteCycles, len(currentMaxChain), currentMaxChain[0]


res = solve() # Store output data

print(__doc__)
print(f"The number of non-ending or infinite cycles: {res[0]}\n")
print(f"The length of the longest series until needing to loop: {res[1]}\n")
print(f"The number that creates the longest series: {res[2]}\n")