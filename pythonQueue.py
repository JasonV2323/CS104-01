names =[]


for i in range(10):
    name=input("Enter a name:")
    names.append(name)

    
    
print(names)

for i in range(len(names)):
    name_removed=names.pop(0)
    print("Name removed: ",name_removed)
    



