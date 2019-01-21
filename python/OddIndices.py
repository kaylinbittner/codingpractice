#Write your function here
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
print(odd_indices([1, 6, 9, -23, 0, 11, 4, 2, 56, -121, 5, -7]))
