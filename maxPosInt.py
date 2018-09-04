num_list = []
while True:
    num_int = int(input("input a number: "))
    num_list.append(num_int)
    if num_int < 0:
        break

max_int = max(num_list)


#get input from user
#get continuous input from user until he puts a negative int
#keep track of highest int and print it out when users inputs a negative int
print("The maximum is", max_int)
#comment