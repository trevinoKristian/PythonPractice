"""
#11
def count(sequence, item):
    count = 0
    for number in sequence:
        if number == item:
            count += 1
    return count

print count([1, 2, 1, 1], 1)


#12
def purify(list_of_nums):
    odd_list = []
    for num in list_of_nums:
        if num % 2 == 0:
            odd_list.append(num)
    return odd_list

print purify([1,2,3])


#13
def product(list_of_ints):
    result = 1
    for num in list_of_ints:
        result *= num
    return result
    

#14
def remove_duplicates(list_of_nums):
    new_list = []
    for num in list_of_nums:
        if new_list.count(num) == 0:
            new_list.append(num)
    return new_list

#15
import math

def median(list_of_nums):
    list_of_nums = sorted(list_of_nums)
    print ("List_of_nums: ") + str(list_of_nums)
    length = len(list_of_nums)
    print ("length: ") + str(length)
    if length == 1:
      return list_of_nums[0]
    #checks for odd lists
    if length % 2 != 0:
        return list_of_nums[int(math.ceil(length/2))]
    else:
        a = length / 2
        print ("a: ") + str(a)
        b = a + 1
        print ("b: ") + str(b)
        if  list_of_nums[a - 1] == list_of_nums[b - 1]:
          return list_of_nums[a - 1]
        else:
          return (list_of_nums[a - 1] + list_of_nums[b - 1]) / (2.0)


print median([4,5,5,4])
"""

grades = [88, 26, 33, 63, 58, 44, 40]

def grades_sum(scores):
  result = 0
  for grade in grades:
    result += grade
  return result

print grades_sum(grades)