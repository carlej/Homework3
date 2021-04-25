import string
def leapYear(a):
	if a%4 == 0:
		if a%400 == 0:
			print("Year is not a Leap Year")
		else:
			print("Year is a Leap Year")
	else:
		print("Year is not a Leap Year")

while True:
	try:
		val = input("Enter a number = ")
		leapYear(int(val));
		break
	except ValueError:
		print("That is not a number.")
