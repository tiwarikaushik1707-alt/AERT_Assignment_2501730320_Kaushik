# AERT Toolkit Assignment
# Data Structures - Unit 1

# ------------------
# Stack ADT
# ------------------

class StackADT:

    def __init__(self):
        self.data = []

    def push(self,x):
        self.data.append(x)

    def pop(self):
        if len(self.data) == 0:
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


# ------------------
# Factorial
# ------------------

def factorial(n):

    if n < 0:
        return "Invalid"

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


# ------------------
# Fibonacci naive
# ------------------

naive_count = 0

def fib_naive(n):

    global naive_count
    naive_count += 1

    if n <= 1:
        return n

    return fib_naive(n-1) + fib_naive(n-2)


# ------------------
# Fibonacci memo
# ------------------

memo = {}
memo_count = 0

def fib_memo(n):

    global memo_count
    memo_count += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1) + fib_memo(n-2)

    return memo[n]


# ------------------
# Tower of Hanoi
# ------------------

def hanoi(n, source, aux, dest, stack):

    if n == 1:
        move = "Move disk 1 from " + source + " to " + dest
        print(move)
        stack.push(move)
        return

    hanoi(n-1, source, dest, aux, stack)

    move = "Move disk " + str(n) + " from " + source + " to " + dest
    print(move)
    stack.push(move)

    hanoi(n-1, aux, source, dest, stack)


# ------------------
# Binary Search
# ------------------

def binary_search(arr, key, low, high, stack):

    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid

    if key < arr[mid]:
        return binary_search(arr, key, low, mid-1, stack)

    return binary_search(arr, key, mid+1, high, stack)


# ------------------
# Main Program
# ------------------

def main():

    print("Factorial Tests")

    nums = [0,1,5,10]

    for n in nums:
        print("factorial(",n,") =", factorial(n))


    print("\nFibonacci Tests")

    tests = [5,10,20,30]

    for n in tests:

        global naive_count
        naive_count = 0

        result1 = fib_naive(n)

        global memo_count
        memo_count = 0
        memo.clear()

        result2 = fib_memo(n)

        print("\nFibonacci",n)
        print("Naive =",result1,"calls =",naive_count)
        print("Memo  =",result2,"calls =",memo_count)


    print("\nTower of Hanoi (n=3)")

    stack = StackADT()

    hanoi(3,"A","B","C",stack)

    print("Total moves stored in stack:",stack.size())


    print("\nBinary Search Tests")

    arr = [1,3,5,7,9,11,13]

    for key in [7,1,13,2]:

        stack = StackADT()

        index = binary_search(arr,key,0,len(arr)-1,stack)

        print("Search",key,"->",index)


    print("\nEmpty list test")

    stack = StackADT()

    res = binary_search([],5,0,-1,stack)

    print("Result:",res)


main()