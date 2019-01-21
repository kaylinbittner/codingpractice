#Write your function here
def over_nine_thousand(lst):
  counter = 0
  if lst == []:
    return 0
  for x in lst:
    if counter <= 9000:
      counter += x
    else:
      return counter
  if counter <= 9000:
    return counter
  
    
    

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([800, 120, 900, 200]))
print(over_nine_thousand([]))
