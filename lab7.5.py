import random as rd
#1

nums = []
for i in range(0,3):
    nums.append(rd.randrange(5,101,5))


print(nums)

#2

nums2 = [1,2,3,4,5,6,7,8,9,10]
nums3 = rd.sample(nums2,3)
print(nums3)

