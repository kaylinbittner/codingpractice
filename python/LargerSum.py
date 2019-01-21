#Write your function here
def larger_sum(lst1, lst2):
  lst1_counter = 0
  lst2_counter = 0
  for a in lst1:
    lst1_counter += a
  for b in lst2:
    lst2_counter += b
  if lst1_counter >= lst2_counter:
    return lst1
  else:
    return lst2
    

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
print(larger_sum([1, 9, 51], [24, 39, 78]))
