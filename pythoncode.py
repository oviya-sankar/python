1)n=int(input("Enter the number:"))
  if n%2==0:
    print("Even number")
  else:
    print("Odd number")

output:
   Enter the number:7
   Odd number


2)n=int(input("Enter a number"))
  if n>0:
    print("positive number")
  elif n<0:
    print("Negative number")
  else:
    print("zero")

output:
  Enter a number22
  Positive number


3)a=int(input("Enter a first number:"))
  b=int(input("Enter the second number:"))
  if a>b:
    print("Largest number is",a)
  elif b>a:
    print("Largest number is",b)
  else:
    print("Both numbers are equal")

output:
  Enter a first number:24
  Enter the second number:27
  Largest number is 27

4)age=int(input("Enter your age:"))
  if age>=18:
    print("Eligible to vote")
  else:
    print("Not eligible to vote")

output:
  Enter your age:19
  Eligible to vote

5)mark=int(input("Enter your mark:"))
  if mark>=35:
    print("Pass")
  else:
    print("Fail")

output:
  Enter your mark:98
  Pass

6)a=int(input("Enter first number:"))
  b=int(input("Enter second number:"))
  c=int(input("Enter third number:"))
  if a>=b and b>=c:
    print("Largest number is",a)
  elif b>=a and b>=c:
    print("Largest number is",b)
  else:
    print("Largest number is",c)

output:
  Enter first number:07
  Enter second number:24
  Enter third number:27
  Largest number is 27
7)year=int(input("Enter a year:"))
  if year%400==0 or(year%4==0 and year%100!=0):
    print("leap year")
  else:
    print("Not a leap year")

output:
  Enter a year:2024
  leap year

8)a=int(input("Enter the first number:"))
  b=int(input("Enter the second number:"))
  print("Addition:",a+b)
  print("Subtraction:",a-b)
  print("Multiplication:",a*b)
  print("division:",a/b)

output:
   Enter the first number:5
   Enter the second number:3
   Addition: 8
   Subtraction: 2
   Multiplication: 15
   division: 1.6666666666666667


9)num=int(input("Enter a number:"))
  if num%5==0:
    print("Divisible by 5")
  else:
    print("Not divisible by 5")

output:
  Enter a number:25
  Divisible by 5


10)age=int(input("Enter your age:"))
   if age>18:
     print("Eligible for student discount")
   else:
     print("Not eligible for student discount")  

output:
   Enter your age:19
   Eligible for student discount
