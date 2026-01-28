# Takes the starting number from users.
First = int(input("Enter the Starting number: "))
# Takes the Ending number form users.
Last =  int(input("Enter the Last number: "))
# Sum starts at 0.
Total = 0
# Range creates a List.
for i in range(First,Last):
# Do the sum.
    Total += i
# This prints the output.
print(f"The sum of {First} to {Last} is:", Total)