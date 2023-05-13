#Loops in python
#for loop
for num in range(1,11):
    print(num)

#example2 for loop with strings
name="Happiness"
for i in name:
    print(i)

#looping with list
students=['akum','happiness','elizabeth', 'richard','mary']
ages=[1,2,3,4,5]
for i in students:
    print(i)
for i in ages:
    if i==4:
        print('hey welcome')
    else:
        print('welcome')
# for loop
for num1 in range(1,21):
    print(num1)

#performing sum of first 10 numbers using for loop(0 to 9)
sum=0
for i in range(1,10):
    sum= sum+i
print('the sum of the numbers is',sum)
# performing sum of the 20 number using for loop (1 to 20)
sum=1
for i in range(1,21):
    sum=sum+i
print("the sum of the number is ",sum) 

#python program to illustrate while loop

count=0
#while(count<3):
    #count=count+1
    #print('Hey Happiness')
while(count<5): count+=1; print('Hey Hapiness welcome')

happi=1
while(happi<5):
    print(happi)
    happi = happi+1
    # While loop
    count=10
    while  count>=1:
     print(count)    
     
     # print even and odd number between 1 to 10
     for i in range (1,10):
         if  i % 2==0:
          print("even number :",i)
     else:
       print('odd number',i)
       
    