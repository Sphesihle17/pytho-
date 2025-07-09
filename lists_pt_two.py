#Adding and removing items on a list

fruits  = ["Apple" , "Cherry", "Mango"]
fruits.append("Avocado") #Add method
print(fruits)

fruits.insert(2,"Kiwi") #Inset method thar specifies where exactly you want to add the item
print(fruits)

fruits.remove("Avocado") #Remove method
print(fruits)


fruits.sort() #Sorts out the items on the list in an ascending order
print(fruits)

fruits.sort(reverse=True) #Sorts out the items on the list in an descending order
print(fruits)


