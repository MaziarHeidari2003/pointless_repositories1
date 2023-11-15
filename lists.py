import os

path = "D:\\Desktop\\all_python_practices\\bitch.txt"

if os.path.exists(path):
    print("that location exists")
    if os.path.isfile:
        print("that is a file")
    elif os.path.isdir:
        print("its a directory")    

else:
    print("nothing!!!")        
