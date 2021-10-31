input_num=int(input('Please enter in a number between 0 and 10000 :'))

  
def maxPermutation(digits):
 maxPermutationNumber=""
 digits.sort(reverse=True)
 for i in range(len(digits)):
    maxPermutationNumber+=str(digits[i])

 print(maxPermutationNumber)


# empty list for storing individual number
digits=[]

def getTheDigit(input_num):
 while(input_num>0):
  digit=input_num%10
  digits.append(digit)
  input_num = input_num //10
 maxPermutation(digits)

 
# **checking input***
if(input_num>10000 or input_num<0):
 print("Please enter an invalid number :")
else:
 getTheDigit(input_num)







