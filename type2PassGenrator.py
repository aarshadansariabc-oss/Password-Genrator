import random

letters = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

special_chars = ['@', '#', '$', '%', '&', '!']

length = int(input("Enter the length of your Password : "))

all_char = letters + numbers + special_chars

password_list = []

for i in range (length):
    password_list.append(random.choice(all_char))

random.shuffle(password_list)

pasword = "".join(password_list)

print(f"Your Password is {pasword}")