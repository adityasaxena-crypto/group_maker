import random
#defining the list variable
list_1 = []

list_2 = []

number_of_items = int(input("How many items do you want to enter? "))

for i in range(number_of_items):
    list_1.append(str(input("Enter an item: ")))

number_of_groups = int(input("How many groups do you want to make? "))

number_items_new_group = int(input("How many items do you want to add to the new list? "))

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
