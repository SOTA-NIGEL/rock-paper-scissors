mylist = ["Tanaka", "Taps", "Nigel"]
print(mylist[1])
print(len(mylist))



mylist[0] = "Simba"
print(mylist)                    # This is how to change an item in a list
print(mylist[1:])              # This is how to print out a list from a certain index to the end

speciallist = mylist[1:]
speciallist.append("Collin")
speciallist.insert(0,"Anna")                  # This is how to add an item to a list according to position
print(speciallist)   

mylist.extend(speciallist)                    # This is how to add a list to another list
print(mylist)





X