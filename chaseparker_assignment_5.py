print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: Sequence: "))
step_count = 0
#CHALLANGE 1 PART
#While loop created for numbers greater than one 
#and tested to see if their even or odd for the Collatz Conjecture sequence, 
#with it ending when the current_number equals 1 with steps counting the time to do this. 
while not(current_number>=1):
   current_number = int(input())


print(int(current_number),end=" ")
while current_number!=1:
  
   if current_number%2==0:
       current_number=current_number/2
  
   else:
       current_number=(3 * current_number) + 1
   step_count+=1
   print(int(current_number),end=" ")
else:
   print()


   print(f"Steps: {step_count}")


   print()


#CHALLANGE 2 PART
#A sequence is created to see if a the numbers given(input_pos) are prime and positive are not
# a variable called is_prime is created to set if its prime
# input_pos is divided based on the numbers before the inputted number 
#and using modulo to see if its prime by seeing if theres a 
#remainded and if not prime, a break is added to simply exit the loop
print('=== Challenge 2: Prime Number Checker ===')


input_pos= int(input())
is_prime=True
print(f"Enter a number: Testing divisors from 2 to {input_pos-1}...")
while input_pos<=0:
   input_pos= int(input())


for i in range(2,input_pos-1):
   if input_pos%i==0:
      is_prime=False
      break
   else:
       is_prime=True
      
        


if is_prime==False:
   print(f"{input_pos} is not prime (divisible by {i})")


if is_prime==True:
   print(f"{input_pos} is prime!")


print()
#CHALLANGE 3 PART
#A set of rows and collumns are created, 
# using numers to determine which row and collumn your on with numbers 
# 1-10 being changed every loop, going from 1--->100,
#  multiplying the row number for that 
# iteration times the column for that iteration
print('=== Challenge 3: Multiplication Table ===')
print('Multiplication Table:')


print("     1   2   3   4   5   6   7   8   9  10")
for rows in range(1,11):
  
   print(f"{rows:2}", end="")
  
   for cols in range(1,11):
       print(f"{rows * cols:4}", end="")
   print()