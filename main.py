import random

letters = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1','2','3','4','5','6','7','8','9','0']

print(type(numbers[0]))


total_letters = int(input("Enter Total number of Letters : "))
total_numbers = int(input("Enter total number of letters : "))

password_list = []
for i in range(0,total_letters):
    password_list.append(letters[random.randint(0,25)])

for i in range (0,total_numbers):
    password_list.append(numbers[random.randint(0,9)])
random.shuffle(password_list)

passw = "".join(password_list)

print(f"Your Password is {passw}")