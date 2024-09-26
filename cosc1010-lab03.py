# Donovan Appelhans
# UWYO COSC 1010
# 9/26/24
# Lab 03 
# Lab Section: 12
# Sources, people worked with, help given to: 
#Introducing lists powerpoint



# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
Midwest_States = ["Wyoming", "Clolorado", "Montana"]


#print the entire list
print(Midwest_States)

#now print the first element in the list
print(Midwest_States[0])

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(Midwest_States[-1])

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
direction = f"{Midwest_States[1]} is south of {Midwest_States[0]}"
print(direction)

print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
East_Coast = []
East_Coast.append("Washington")
East_Coast.append("Oregon")
East_Coast.append("California")
print(East_Coast)
#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
East_Coast[-2] = "Maine"
print(East_Coast)

#Insert the state Texas to be the third element in the list, again printing your list
East_Coast.insert(2,"Texas")
print(East_Coast)

#Using the `del` statement remove the fourth item from the list, print your list 
del East_Coast[-1]
print(East_Coast)

#Remove Texas using its value, print the list
East_Coast.remove("Texas")
print(East_Coast)

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(East_Coast)
print(sorted(East_Coast))

#Permanently sort your list in reverse order, printing it out
East_Coast.sort()
print(East_Coast)

#Using the reverse method reverse the list and print it
East_Coast.sort(reverse=True)
print(East_Coast)

