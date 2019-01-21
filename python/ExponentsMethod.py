#Write your function here
def exponents(bases, powers):
  new_lst = []
  for b in bases:
    for p in powers:
      new_lst.append(b**p)
  return new_lst
      

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
print(exponents([4, 5, 6], [1, 2, 3]))
