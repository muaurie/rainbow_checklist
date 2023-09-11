checklist = list() 
#checklist = [] #less explicit 
#checklist.append('Blue')
#print(checklist)
#checklist.append('Orange')
#print(checklist)

def create(item): #create
    checklist.append(item)
def select(function_code):
     #create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)
    #read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        
        #remember item_index must exist or crash
        read(item_index)
    #print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "Q":
        return False
    #if all else fails
    else:
        print("Unkown Option")
    return True
    
    

def mark_completed(index):
   checklist[index] = "[√]" +checklist[index]
   print(read(index))
def read(index): #read
   if 0 <= index < len(checklist): #use len to check the length of the checklist
    return checklist[index]
   else: 
      return "Index out of range"
def update(index, item):
    if 0 <= index < len(checklist):
        checklist[index] = item
    else: 
      return "Index out of range"
def destroy(index): #destroy
    if 0 <= index < len(checklist):
        checklist.pop(index)
    else:
        print("Index out of range")
def list_all_items():
    index = 0 #func in this code require an index number
    for list_item in checklist:
    #   print(str(index) + list_item)
        print("{} {}".format(index, list_item))
    index += 1 #add one to index for each item
def user_input(prompt):
    #prompt the user for input
    user_input = input(prompt)
    return user_input
def test():
    user_value = user_input("Please enter a value")
    print(user_value)

test()



running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list, P to display list, and Q to quit")
    running = select(selection)

    
#checklist = ['Blue', 'Orange']
#checklist[1] = 'Cats' #assigning Cats to the number of 1 within the array
#print(checklist)


