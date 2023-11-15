#try:
   # with open('bitch.txt') as file:
    #   print (file.read())
#except FileNotFoundError:
 #   print("that file was not found")
#print(file.closed)    

text = "yoooo\n this is some new text\n"
with open('text.txt','w') as file:
    file.write(text)