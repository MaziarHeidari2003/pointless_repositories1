def hello(**kwargs):
  print("hello",end=" ")
  for key,value in kwargs.items():
      print(value, end=" ")


hello(title="mr",first="ali", middle="bitch" , last="hosseini")