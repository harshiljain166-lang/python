# n=int(input("enter the table you want   :    "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")
 


# n=int(input("enter number  : "))
# s=0
# for i in range(1,n+1):
#     s=s+i
#     print(f" your sum is {s}")


n=int(input("tell your range   : "))
even_sum=0
odd_sum=0
for i in range(1,n+1):
    if i%2==0:
        even_sum=even_sum+i
    else:
        odd_sum=odd_sum+i
print(f"your evensum is {even_sum} \n your oddsum is {odd_sum}")        