first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  last_three = first_name[len(first_name)-3:] + last_name[len(last_name)-3:]
  return last_three

temp_password = password_generator(first_name, last_name)

print(temp_password)
