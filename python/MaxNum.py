#Write your function here
def max_num(nums):
  maximum = nums[0]
  for n in nums:
    if n > maximum:
      maximum = n
  return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
