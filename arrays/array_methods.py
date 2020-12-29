# array methods


# reverse an array
def reverseArray(a):
    # we know we're taking in an array that looks like this: [0,1,2,3,4]
    # we want it to become [4,3,2,1,0]
    
    # instantiate a new structure
    return_array = []

    # initialize a counter
    i = len(a)-1

    # because the array is 0 indexed, an array with 5 elements will have i set to 4
    # this will stop after it adds the first (0) element
    while (i > -1):
        return_array.append(a[i])
        i = i - 1
        
    return return_array