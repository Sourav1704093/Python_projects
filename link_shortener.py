import pyshorteners

user_link = input("Enter the link you wanna short: ")

short = pyshorteners.Shortener()

gen_link = short.tinyurl.short(user_link)

print(gen_link)