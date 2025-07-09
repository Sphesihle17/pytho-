#OUR SHOOPING CART PROGRAMME

#Step one create variables to store our items
foods = []
prices = []
total  = 0

#Create a loop so that the user can continuesly add products

while True:
    food = input("Enter the items you want to purchase or press q to quit: ")
    if food.lower() == 'q':
        break
    
    else:
        price = float(input(f"Enter the price of the {food}: R ")) 
        foods.append(food)
        prices.append(price)
         
print ("...YOUR CART...")     

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print("\n")    
print(f"Your total is: R{total}")      
        
        