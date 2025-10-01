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