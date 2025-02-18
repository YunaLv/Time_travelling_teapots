import random

# Use these lists to try this out
sorted_numbers = [3, 7, 8, 15, 23, 45, 67, 78, 89, 97]
new_numbers = [42, 9, -4, 99, 98]

for tosort in new_numbers:
    for number in sorted_numbers:
        if number > tosort:
            index = sorted_numbers.index(number)
            sorted_numbers.insert(index, tosort)
            break
    else:
        sorted_numbers.append(tosort)
#print (sorted_numbers)

sorted_number = []
unsorted_numbers = [42, 9, -4, 99, 15, 97, 78, 23, 67, 3, 89, 45, 8, 7]

for tosort in unsorted_numbers:
    for number in sorted_number:
        if number > tosort:
            index = sorted_number.index(number)
            sorted_number.insert(index, tosort)
            break
    else:
        sorted_number.append(tosort)
#print (sorted_number)


number_list = []
i=0
while i<100:
    number_list.append(random.randint(-1000,1000))
    i+=1
#print (number_list)

sorted_number3 = []

for tosort in number_list:
    for number in sorted_number3:
        if number > tosort:
            index = sorted_number3.index(number)
            sorted_number3.insert(index, tosort)
            break
    else:
        sorted_number3.append(tosort)
print (sorted_number3)

sorted(number_list)
print (sorted(number_list))
if sorted(number_list) == sorted_number3:
    print ("yay")
else:
    print ("boo")