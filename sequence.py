n = int(input("Enter the length of the sequence: ")) # Do not change this line
#figure out how to implement the sequence.
#make n decide how many numbers in the sequence are printed
tala1 = 1
tala2 = 2
tala3 = 3
sum = 0
for i in range(1,n+1):
    if i == 1 or i == 2 or i == 3:
        print(i)
    else:
        sum = tala1 + tala2 + tala3
        print(sum)
        tala1 = tala2
        tala2 = tala3
        tala3 = sum


#1       2     3     6   11  20
#tala1 tala2 tala3  sum

#       tala1 tala2 tala3


#print()