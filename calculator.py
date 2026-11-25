print("Student Grade Calculator")
mark1 = float(input("Enter first mark: "))
mark2 = float(input("Enter second mark: "))
mark3 = float(input("Enter third mark: "))
average = (mark1 + mark2 + mark3) / 3
print(f"Average: { average:.2f}%")
if average >= 50:
	print("Result: Pass")
else:
	print("Result: Fail")

