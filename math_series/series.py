import math
import sys
sys.setrecursionlimit(10**9)

def fibonacci(n):
#     """The order goes as follows: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 and on to infinity.
#      Each number is the sum of the previous two. This series of numbers is known as the Fibonacci numbers or the Fibonacci sequence """

#  """"The fucntion starts here checking that the input/test case covers the base values""""
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        # """" After covring the base value the looping start fiving the sum of the 2 numbers before the value of n on repeate
        # so if we say n = 4
        # it will go like  fibonacci(3)+fibonacci(2)
        #  fibbonaci(3) is fibonacci(2)+fibonacci(1) and it keeps going until it reaches the base case and sums back up""""
        return fibonacci(n-1)+fibonacci(n-2)

def lucas(n) :
    # """ Lucas numbers are the same as febonacci when it comes to the formula but they are
    # diffrent at the base (lucas numbers start at 2,1) """

    if (n == 0) :
        return 2
    if (n == 1) :
        return 1
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n,x=0,y=1):
    # """This function is to use either the lucas formula or the fibonacci one based on optional arguments
    # if the input of x is 2 and y is one that means the result is wanted in lucas form and so the lucas funtion will be used
    # other wise if the optinal arguments are not used or given the base stats of the fibonacci formula the fibonacci method will be used by default   """
    if x == 0:
      return fibonacci(n)
    elif x ==2:
       return lucas(n)
    else:
        if x < y:
          if n == x:
              return x
          elif n ==y:
              return y
          else:
              return sum_series(n-1,x,y)+sum_series(n-2,x,y)
        else:
            return "input a right base"


print(sum_series(7,3,4))

