data = list(input("enter value :"))
print(data)
copy_1 = data.copy()
copy_1.reverse()
print(copy_1)
if(copy_1 == data):
    print("palindrome")
else:
    print("not palindrome")    