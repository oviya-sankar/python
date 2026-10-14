1)count=0
    for i in range(1,51):
       if i%5==0:
          count+=1
    print("count=",count)

output:
     count= 10

2)total=0
   for i in range(1,21):
      if i%2!=0:
           total+=i
   print("sum=",total)

output:
       sum= 100

3)for i in range(1,31):
    if i%3==0 and i%4!=0:
         print(i,end=" ")  

output:
     3 6 9 15 18 21 27 30 

4)pos=0
   neg=0
   for i in range(5):
       n=int(input("Enter number:"))
       if n>0:
            pos+=1
       elif n<0:
           neg+=1
    print("Positive=",pos)
    print("Negative=",neg)

output:
     Enter number:-7
     Enter number:2
     Enter number:-4
     Enter number:7
     Enter number:1
    Positive= 3
    Negative= 2

5)a=int(input("Enter first number:"))   
    b=int(input("Enter second number:"))   
    c=int(input("Enter third number:"))   
    if a>=b and a>=c:
       print("Largest number=",a)
   elif b>=c:
      print("Largest number=",b)
   else:
      print("Largest number=",c)

output:
        Enter first number:11
        Enter second number:7
        Enter third number:27
        Largest number= 27

6)n=int(input("Enter number:"))
   fact=1
   for i in range(1,n+1):
     fact=fact*i
   print("Factorial=",fact)  

output:
       Enter number:7
       Factorial= 5040

7)n=int(input("Enter number:"))
   count=0
   for i in range(1,n+1):
      if n%i==0:
          count+=1
    if n>1 and count==2:
       print("prime number")
   else:
      print("Not a prime number")
  
output:
     Enter number:4
     Not a prime number

8)n=int(input("Enter the four digit number:"))
   total=0
   while n>0:
      digit=n%10
      total+=digit
      n//=10
   print("sum=",total)  

output:
      Enter the four digit number:9510
      sum= 15
 
9)for i in range(1,11):
        if (i*i)%2==0:
            print(i,end=" ")

output:
      2 4 6 8 10 

10)n=int(input("Enter number:"))
      temp=n
      total=0
      digits=len(str(n))
      while temp>0:
          digit=temp%10
          total+=digit**digits
          temp //=10
     if total==n:
          print("Amstrong number")
     else:
          print("Not Amstrong number")
  
output:
      Enter number:1324
      Not Amstrong number
1)n=int(input("Enter the number:"))
   sq=n*n
  if str(sq).endswith(str(n)):
      print("Automorphic number")
  else:
     print("Not an automorphic number")

output:
     Enter the number:8675
     Not an automorphic number

2)n=int(input("Enter a number:"))
   sq=n*n
   s=sum(int(d)for d in str(sq))
   if s==n:
      print("Neon number")
   else:
      print("Not a Neon number")

output:
     Enter a number:1
     Neon number

3)n=int(input("Enter a number:"))
   s=0
   for i in range(1,n):
       if n%i==0:
           s+=i
   if s==n:
      print("Perfect number")
  else:
     print("Not a perfect number")
 
output:
       Enter a number:69087
       Not a perfect number

4)n=input("Enter a number:")
   if n==n[::-1]:
      print("Palindrome number")
  else:
     print("Not a Plindrome")

output:
       Enter a number:7
       Palindrome number

       
