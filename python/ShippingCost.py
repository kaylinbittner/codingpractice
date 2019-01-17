flat_charge = 20

def ground_shipping_cost(weight):
  if weight <= 2: 
    return (1.50 * weight) + flat_charge
  elif (weight > 2) and (weight <= 6):
    return (3 * weight) + flat_charge
  elif (weight > 6) and (weight <= 10):
    return (4 * weight) + flat_charge
  else:
    return (4.75 * weight) + flat_charge
  
def drone_shipping_cost(weight):
  if weight <= 2: 
    return (4.50 * weight)
  elif (weight > 2) and (weight <= 6):
    return (9 * weight)
  elif (weight > 6) and (weight <= 10):
    return (12 * weight)
  else:
    return (14.25 * weight)
  
def cheapest_shipping_cost(weight):
  if ground_shipping_cost(weight) < drone_shipping_cost(weight):
    return "Ground shipping is the cheapest method of shipping your package. It would cost $" + str(ground_shipping_cost(weight)) + " to ship your package."
  elif ground_shipping_cost(weight) > drone_shipping_cost(weight):
    return "Drone shipping is the cheapest method of shipping your package. It would cost $" + str(drone_shipping_cost(weight)) + " to ship your package." 
  else:
    return "The cost of shipping your package is the same - regardless of the shipping method. It would cost $" + str(drone_shipping_cost(weight)) + " to ship your package."

print(ground_shipping_cost(8.4))
print(drone_shipping_cost(1.5))
print(cheapest_shipping_cost(41.5))
