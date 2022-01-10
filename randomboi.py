import random
#defining the list variable
list_1 = []
modd = 0
list_2 = []
number_of_items = int(input("How many items do you want to enter? "))

anwser_1 = input(str("Would you like to tell me the number of people in the group? (y/n)")).lower()
if anwser_1 == "y":
    number_items_new_group = int(input("Number of people in each group?"))

for i in range(number_of_items):
    list_1.append(str(input("Enter an item: ")))



anwser = str(input("Do you want to tell number of groups (y/n) "))

if anwser == "y":
    number_of_groups = int(input("How many groups do you want to make? "))
elif anwser == "n":
    if(number_of_items % number_items_new_group == 0):
        number_of_groups = int(number_of_items / number_items_new_group)
    else:
        modd = number_of_items % number_items_new_group
        print("Number of people in the last group is: ", modd)
        number_of_groups = int((number_of_items-modd) / number_items_new_group) 

for j in range(number_of_groups):
    for i in range(number_items_new_group):
        
        length  = len(list_1)

        if length == 0:
            print("No more items to choose from!")
            break
        else:
            random_number = random.randint(0, length - 1)
            list_2.append(list_1[random_number])
            del list_1[random_number]

        
    print(list_2)
    list_2 = []

print("The remaining people are: ", list_1)