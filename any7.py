def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    for num in nums:
        if num == 7:
            return True
    return False

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]

evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)

print(evens)
# [2,4,6,8,10,12]

# with list comprehension, this statement can be much shorter
evens = [num for num in nums if num % 2== 0]

doubled = [num * 2 for num in nums]

#new list = [what we want, for each item in original list, #optional conditional statement]

#nested = [[initial_val for x in range(n)] for y in range(n)]

#[x for x in range(10)]
# [0,1,2,3,4,5,6,7,8,9]

#[x for x in range(10) if x % 2== 0]
#[2,4,6,8]

# Dictionary and Set Comprehensions:
dict = {day: 0 for day in "MTWRFSU"}

nums_dict = {num: num ** 2 for num in range(1,10)}
print(nums_dict)