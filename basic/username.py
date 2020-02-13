s = 'Hello <<username>>, How are you?'
print(s)
print("Enter your name:")
name = input()
print(s.replace("<<username>>",name))