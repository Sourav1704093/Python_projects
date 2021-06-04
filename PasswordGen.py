import random

upperLetter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #which includes uppercase letter in generated password
lowerLetter = "abcdefghijklmnopqrstuvwxyz" #which includes lower case letter in generated password
digit = "0123456789" # it will include digits in password
special_char = "!@#$%^*(){}[],<>?;:/" # it will make our generated password strong 

up,low,nums,symbol = True,True,True,True # which will use all the combination of letter,digits and special symbols

gen_pass = "" # just a empty string

if up:
    gen_pass += upperLetter
if low:
    gen_pass += lowerLetter
if nums:
    gen_pass += digit
if symbol:
    gen_pass += special_char

pass_length = 15 # describes password length

pass_amount = int(input()) # how many password you wanna generate

for _ in range(pass_amount):
    password = "".join(random.sample(gen_pass,pass_length))
    print(password)
    
