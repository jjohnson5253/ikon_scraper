import sys
import checkAvail

def constantCheck():
	while(1):
		if (checkAvail.checkAvail(pwInput, monthInput, dayInput, yearInput) == true):
			# send email and/or make reservation

def main():
	# get user input for date and password
	pwInput = sys.argv[1]
	monthInput = sys.argv[2]
	dayInput = sys.argv[3]
	yearInput = sys.argv[4]

	checkAvail.checkAvail(pwInput, monthInput, dayInput, yearInput)
	sys.exit()

if __name__ == "__main__":
    main()