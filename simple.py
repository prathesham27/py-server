mylist = input("Enter The Input:")
list = mylist.split()
print("Input:", list)
for x in mylist:
    if len(set(list)) == len(list):
        print("True")
    else:
        print("False")
