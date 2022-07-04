from datetime import date


def get_dob(year, month, day):
    # write code here
	...
year=int(input("Enter your year of birth: "))
month=int(input("Enter your month of birth: "))
day=int(input("Enter your day of birth: "))
dob=date(year, month, day)
# print(dob)


def get_age(dob):
    # write code here
	...
today=date.today()
age=today-dob
ageinyears=(age.days//365)
if ageinyears <= 0:
	print("You are not born yet")
else:
	print("You are", str(ageinyears), "years old")



def main():
	# write code here
	...


if __name__ == '__main__':
    main()
