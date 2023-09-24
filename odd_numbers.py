# print all the odd numbers between min_num and max_num
min_num, max_num = map(int, input("Enter two integers: ").split())

if min_num % 2 == 0:
    min_num += 1

for i in range(min_num, max_num + 1, 2):
    print(i)
