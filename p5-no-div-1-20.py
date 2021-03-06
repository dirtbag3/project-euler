def traditional():
    # Taking the entire list
    l = range(2, 21)

    # Doing this the old C++ style
    # Initializing the pointer to first element
    i = 0

    # Traversing the entire list
    while i < len(l):
        # Starting the next element in the list
        j = i + 1
        while j < len(l):
            # Checking if L[j] is completely divisible by L[i] 
            if l[j] % l[i] == 0:
                # If yes, replace L[j] by L[j]/L[i]
                # This is just normal reduction
                l[j] = l[j] / l[i]

            j = j + 1

        i = i + 1

    # Finding the product of the list
    ans = reduce(lambda x, y: x * y, l)
    return ans

print "Answer by traditional method:", traditional()
