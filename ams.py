low= int(input(""))
upp= int(input(""))
 
for num in range(low,upp + 1):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
