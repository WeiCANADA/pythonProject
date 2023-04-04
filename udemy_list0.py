answer2 =[i  for i in [1,2,3,4,5,6] if i%2 == 0]

'''
For all the numbers between 1 and 100(including 100), create a variable called answer, which contains a list with all the numbers that are divisible by 12.  (12, 24, etc)
'''
answer = [i for i in range(1,101) if i%12 == 0]
print(answer)

'''
Given the string "amazing", create a variable called answer,
 which is a list containing all the letters from "amazing"
  but not the vowels (a, e, i, o, and u).  The answer should look like: ['m', 'z', 'n', 'g'].
'''
answer = [char for char in 'amazing' if char not in 'aeiou' ]
print(answer)