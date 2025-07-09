 #using break with while loops
count = 0
while count< 5:
    print(count)
    count += 1
    if count == 3:
        break
    
    
    
#using break
    print()
    
    fruits  = ["apple", "bananna ", "cherry", "orange", "pineapple"]

for fruit in fruits :
    if fruit  == "orange" :
        break #This will exit the loop  if orange is found
    print(fruit)
    
    
    
    
#using continue
    print()
    fruits  = ["apple", "bananna ", "cherry", "orange", "pineapple"]
    
for fruit in fruits :
    
    if fruit  == "orange" :
        continue #This will exit the loop  if orange is found
    print(fruit)
    
    
    
    
    
#using pass
    print()
    fruits  = ["apple", "bananna ", "cherry", "orange", "pineapple"]

for fruit in fruits :
    if fruit  == "orange" :
        pass #This will exit the loop  if orange is found
    print(fruit)
    