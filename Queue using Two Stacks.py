# Queue using Two Stacks

# HackerRank Problem Solved using Python.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l1 = []
for i in range(n):
    a = input()

    if " " in a:
        l, m = a.split(" ")
        if (l == "1"):
            l1.append(m)
    if (a == "2"):
        b = l1[0]
        l1.remove(b)
    if (a == "3"):
        print(l1[0])
