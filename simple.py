mylist = input("Enter The Input:")
list = mylist.split()
print("Input:", list)
for x in mylist:
    def unique(list):
        if len(set(list)) == len(list):
            return True
        else:
            return False
if(unique (list) == True):
    print("TRUE")
elif(unique (list) == False):
    print("FALSE")




