from math import ceil

def bucketSortAlgo(array, bucketNum):
    """
    Implementing the bucket sorting algorithm into a program.
    """
    buckets = [[] for x in range(bucketNum)]

    largestValue = max(array)
    interval = largestValue/bucketNum

    for x in array:
        buckets[ceil(x / interval) - 1].append(x) 
    for y in buckets:
        y.sort()      
    return [z for temp in buckets for z in temp]
 
presort = []
bucketNumInput = int(input("Insert number of buckets: "))
numberInput = input("Insert first number: ")
while numberInput != '':
    presort.append(int(numberInput))
    numberInput = input("Insert next number (empty to stop): ")

end = bucketSortAlgo(presort, bucketNumInput)
test = end == sorted(presort)

print(f"\n{test}\n")
print(f"The final sorted result is {end}\n")

#Time complexity of bucket sort is O(n+k)
#O(n)
