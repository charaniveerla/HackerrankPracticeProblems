"""
                                                                          ---------------------------------------------------
                                                                          TCS Digital Previous Year Advanced Coding Question
                                                                          ---------------------------------------------------
                                                                          
Question: Find the smallest number whose digits multiply to a given number n
---------

Explanation: Given a number ‘n’, find the smallest number ‘p’ such that if we multiply all digits of ‘p’, we get ‘n’. The result ‘p’ should have minimum two digits.
------------

Examples:  
---------

Input:  n = 36
Output: p = 49 
// Note that 4*9 = 36 and 49 is the smallest such number

Input:  n = 100
Output: p = 455
// Note that 4*5*5 = 100 and 455 is the smallest such number

Input: n = 1
Output:p = 11
// Note that 1*1 = 1

Input: n = 13
Output: Not Possible

APPROACH FOLLOWED:
-----------------
1. There are basically three cases that you need to take care about.
    a) For input numbers <=9 i.e., single digit numbers
    b) For input numbers >=10 
    c) For input numbers which are prime i.e., they dont have any other factors except 1 and the number itself
2. For 1)a) Just add 10 to the input number so that the product of digits in the sum of input number and 10 is same as the input number.
   For 1)b) Since we want individual digits product, to be equal to the input number, Check if 1 to 9 numbers are dividing the given input number. 
   Now just like how we do in prime factorisation, if ith number divides n, then send that ith number to resultant list, and update the n value by dividing with ith number.
   Now print the reverse of the resultant list
   For 1)c) if n from the above step did not become <=9 or if it is >10 then simply print "Not Possible" i.e., the given input number is exactly prime. So it doesn't have any factors.
   
"""
n=int(input())
if(n<=9):
    print(n+10)
else:
    res=[]
    for i in range(9,1,-1):
        while(n%i==0):
            res.append(i)
            n=n/i
    if(n>10):
        print("Not Possible")
    else:
        rev=0
        for i in range(len(res)-1,-1,-1):
            rev=(rev*10)+res[i]
        print(rev)
