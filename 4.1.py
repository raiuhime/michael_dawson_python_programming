# Counting program that allows user to enter the starting number, the ending number and the amount by which to count

print('Hello! Welcome to Counting program!\n')

start = int(input("Enter the starting number:"))
end = int(input("Enter the ending number:"))
step = int(input("Enter the interval:"))

for i in range(start, end, step):
    print(i)
