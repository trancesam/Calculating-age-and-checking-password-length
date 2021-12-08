#exercise- calculating age
year=input('In which year you were born?')
present=input('Insert the present year.')
age=int(present)-int(year)
age1=str(age)
print('Your age is {}' .format(age))

#exercise- password checker
username=input('Enter the username\t')
password=input('Enter the password\t')
hide='#'*len(password)
print('Hey {}, your password {} is {} characters long' .format(username,hide,len(password)))