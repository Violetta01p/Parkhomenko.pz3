num_str = input("Enter number separated by commas: ")
num = [float(num.strip()) for num in num_str.split(",")]
sum_num = sum(num)
average = sum_num / len(num) if num  else 0
print("Sum: {sum_numbers}")
print("Average : {average}")
