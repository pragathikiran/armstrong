print("enter  a number to check if it a amstring number")
num = int(input("enter a number here"))
power = len(str(num))
armstrong_sum = sum(int(digit)**power for digit in str(num))
if num == armstrong_sum:
    print("its a armstrong number")
else:
     print("this is not a armstrong number")