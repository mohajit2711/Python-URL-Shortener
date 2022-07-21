import pyshorteners

# Sample URL - https://github.com/mohajit2711/Python-URL-Shortener - Github Repo


print("Hello, Welcome to Mohajit's URL shortener terminal! ")

print("\n")

long_link = input("Please enter the link you would like to shorten: ") #Asking for Long URL input

pyshort = pyshorteners.Shortener() #using pyshorteners package

short_link = pyshort.tinyurl.short(long_link) #shortening URL

print("The shortened link is: " + short_link) #Shortened link displayed.


# This code is contribute by Mohajit Paul
