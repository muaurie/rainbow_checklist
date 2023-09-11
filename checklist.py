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
    #if all else fails
    else:
        print("Unkown Option")
    

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
def test():

    create ("purple socks")
    create ("red cloak")
    
    print (read(0))
    print (read(1))
#call other funcs
    mark_completed(1)

    destroy(1)

    list_all_items()
  #  update(0, "purple socks")
  #func code
    select("C")

    list_all_items()

    select("R")

    list_all_items()

test()
    
#checklist = ['Blue', 'Orange']
#checklist[1] = 'Cats' #assigning Cats to the number of 1 within the array
#print(checklist)


