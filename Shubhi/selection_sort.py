unsorted_numbers = [42, 9, 99, 15, 97, 78, 23, 67, 3, 89, 45, 8, 7]
sorted = []
while len(unsorted_numbers)>0:
    for number in unsorted_numbers :
        sorted.append (min(unsorted_numbers))
        indexed = unsorted_numbers.index(min(unsorted_numbers))
        unsorted_numbers.pop(indexed)
print (sorted)

