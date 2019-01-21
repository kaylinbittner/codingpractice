#Write your function here
def divisible_by_ten(nums):
  count = 0
  for n in nums:
    if n % 10 == 0:
      count += 1
    else:
      count += 0
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
