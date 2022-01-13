'''
def testgen(index):
    weekdays = ['sun','mon','tue','wed']
    yield weekdays[index]
    yield weekdays[index+1]

day = testgen(0)
print(next(day),next(day))

#Convert list into string

weekday = ['sun','mon','mon','tue','wed','thurs','fri','sat']
stringvariable = ''.join(weekday)
print(stringvariable)

#Convert list into tuple

listastuple = tuple(weekday)
print(listastuple)

#Convert list into set

listasset = set(weekday)
print(listasset)

#Count occurences of particular elements in a list
weekday = ['sun','mon','mon','tue','wed','thurs','fri','sat']

print(weekday.count('mon'))

print([[x,weekday.count(x)] for x in set(weekday)])

import array 

a = [1,2,3]
print(a[-3])

names = ['Chris','Jack','John','Daman']
print(names[-3][-1])

subjects = ('Python','Interview','Questions')
for i, subject in enumerate(subjects):
    print(subject)

objects = {'Python','Coding','Tips','For','Beginners'}

print(objects)
print(len(objects))

if 'tips' in objects:
    print('These are python programming tips')

if 'Java tips' not in objects :
    print("These are the best python coding tips not java tips")

items = set()

items.add('Python')

print(items)

import random 

print(random)
print(random.uniform(1,2))
print(random.randint(1,67))


n = int(input("Enter Number : "))
temp = n 
rev = 0
while(n>0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n//10
if(rev==temp):
    print("The number is palindrome")


a = int(input("Enter Number : "))
k = 0
for i in range(2,a//2+1):
    if(a%i==0):
        k=k+1
if(k<=0):
    print("Number is prime")
else:
    print("Number isn't prime")

n = int(input("Enter the number to print the tables for : "))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
'''

import time
from plyer import notification

if __name__ == '__main__':
    #while True:
    notification.notify(
        title = "Please Drink Water",
        message = "You should drink atleast 3.7 litres of water which will greatly benefit you",
        app_icon = (r"C:\Users\mpush\Videos\5-Python-Projects\Drink-Water-Notification\Water-Glass.ico"),
        timeout = 5
    )
        #time.sleep(2*60*60)

