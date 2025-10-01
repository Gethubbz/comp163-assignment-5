print("=== Challenge 1: Collatz Conjecture ===")
current_number = int(input("Enter starting number: Sequence: "))
step_count = 0


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
print('=== Challenge 3: Multiplication Table ===')
print('Multiplication Table:')


print("     1   2   3   4   5   6   7   8   9  10")
for rows in range(1,11):
  
   print(f"{rows:2}", end="")
  
   for cols in range(1,11):
       print(f"{rows * cols:4}", end="")
   print()