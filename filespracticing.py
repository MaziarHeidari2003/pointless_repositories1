#try:
   # with open('text.txt') as file:
    #    print(file.read())

#except FileNotFoundError:
 #   print("that file was not found")

#text = "yoo\n this is some text \n so how are you\n"
#with open('practice.txt', 'w') as file:
   # file.write(text)

#import shutil 
#shutil.copyfile('text.txt','copy.txt')

#import os

#source = 'copy.txt'
#destination = 'D:\\Desktop\\replacement.txt'
 #try:

    #if os.path.exists(destination):
     #   print("there is already a file in there")
   # else:
       # os.replace(source,destination)
      #  print(source+ "was moved")    
 

 #except FileNotFoundError:
  #      print(source+" was not found")



import os
import shutil

path = 'folder1'
try:  
   # os.rmdir(path)
   shutil.rmtree(path)

except FileNotFoundError:
    print("that file wasnt found") 
except PermissionError:
    print('no bitch, no!!!')
except OSError:
    print('you are using the wrong function asshole')    
else:
    print('path was deleted')      
