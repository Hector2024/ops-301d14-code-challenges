'''
Create a Python script that includes the following:

    Assign to a variable a list of ten string elements.
    Print the fourth element of the list.
    Print the sixth through tenth element of the list.
    Change the value of the seventh element to “onion”.
'''
#variable
ten_things = ["pizza", "ice cream", "lettuce", "tomato", "rollerblade", 
              "ice", "hotpocket", "beer", "wine", "baseball"]


#prints the list
print(ten_things)

#prints the fourth element @index 3
print(ten_things[3])

#prints the elements from 6-10
print(ten_things[5:11])

#changes the 7th element which is at index 8 from "wine" to "onion"
ten_things[8] = "onion"

#prints new item at index 8
print(ten_things[8])


#prints the list again
print(ten_things)