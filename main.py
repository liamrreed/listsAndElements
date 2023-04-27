'''
string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []
print(string_list)
print(int_list)
print(float_list)
print(boolean_list)
print(mixed_list)
print(empty)
'''

# a list of menu items
food = ["Burger", "Shake", "Fries"]

print(food[0], "is located at index 0.")
print(food[1], "is located at index 1.")
print(food[2], "is located at index 2.")
print(food[-1], "is located at index -1")

if ("Sundae" in food):
  print("One sundae, coming up!")
else:
  print("Sorry, we don't carry sundaes")

if ("Shake" in food):
    print("One shake, coming up!")
else:
    print("Sorry, we don't carry shakes")

if ("Fries" in food):
    print("One fries, coming up!")
else:
    print("Sorry, we don't carry fries")

if ("Burger" in food):
    print("One burger, coming up!")
else:
    print("Sorry, we don't carry burgers")
if ("Pizza" not in food):
    print("Pizza is not served.")

customer_order = ["Fries", "Shake"] 
item = input("What else would you like to order? ") 
customer_order.append(item) #appends "item" to customer order

print("You ordered", customer_order) 
answer = input("Is your order correct? ") 
if (answer == "yes"): 
  print("Great! Your order is coming right up!") 
else: 
  print("Okay, I will remove", item, "from your order.") 
  customer_order.remove(item) #removes "item" from customer order

print("Your new order is", customer_order)
