word = input("Word? ")
key = int(input("Key? "))
foo = 97

caesarShift = ''.join([chr(((ord(i)+key-foo)%26)+foo) for i in word])

print(caesarShift)