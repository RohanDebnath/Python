#  Python credit card validation program

# 1. Remove any '-' or ' '
# 2. Add all digits in odd places from right to left
# 3. Double every second digit from left to right
#     (If the result is a two digit add the digit to get a single digit)
# 4. Sum the total of steps 2 & 3
# 5.  If the sum is divisible by 10, the credit card is valid

card_number=input("Enter your card number ")
print(card_number)
card_number=card_number[ : :-1] #Reverse korche
print(card_number)
sum=0
digitSumEven=0
digitSumOdd=0
card_number=card_number.replace("-","") 
card_number=card_number.replace(" ","")
for i in card_number[::2]:  #odd
    digitSumOdd+=int(i)
for i in card_number[1::2]: #even
    x=int(i)*2
    if x>10:
        digitSumEven+=(1+(x%10))
    else:
        digitSumEven+=x
sum=digitSumEven+digitSumOdd
if(sum%10==0):
    print("Valid")    
else:
    print("Invalid")
