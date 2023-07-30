################################
# Title for your program: Looking for Fermat’s Last Theorem Near Misses
# Name of the program file: NearMisses.py
# External files necessary to run the program: None
# Eternal files the program creates: NearMisses.exe- Executable binary for windows OS
# Names of programmers: Balaramakrishna Yadav Keerthi and Prem Sai Reddy Nallamalapu
# Email address: BalaramakrishnaYad@lewisu.edu and PremSaiReddyNallam@lewisu.edu
# Course number and section number of the: Software Engineering(SU23-CPSC-60500-001)
# Date: 29 July 2023
# Explanation: program that helps an interactive user search for “near misses” of the
# 			form (x, y, z, n, k) in the formula xn + yn = zn, where x, y, z, n, k are
# 			positive integers, where 2< n <12, where 10 <= x <= k, and where 10 <= y <= k.
# Language: python3
################################

def near_misses(n, k):
	# clalculate Fetmat's Theorem near misses

	# initialize minimum value of realtive miss
	relative_miss_min = None
	# print result heading
	print("=========================================================================================================")
	print("|\tIndex\t|\tX\t|\tY\t|\tZ\t|\tMiss\t  |\tRelative Miss %\t|")
	print("=========================================================================================================")
	it=0
	for x in range(10, k):
		for y in range(10, k):
			# calculate the miss
			xyn = pow(x, n) + pow(y, n)
			z = int(pow(xyn, 1/n))
			zn = pow(z, n)
			z1n = pow(z+1, n)
			miss = min(xyn-zn, z1n-xyn)
			# claculate relative miss
			relative_miss = miss/xyn
			# update relative miss min value when a new minimum value calculated or for the first time
			if relative_miss_min is None or relative_miss<relative_miss_min:
				relative_miss_min = relative_miss
				it+=1
				# print results
				print(f"|\t{it}\t|\t{x}\t|\t{y}\t|\t{z}\t|\t{miss}\t  |\t{round(relative_miss_min*100,2)}\t\t|")
				print("---------------------------------------------------------------------------------------------------------")

	# print Final result
	print("=========================================================================================================")
	print(f"|\tFinal\t|\t{x}\t|\t{y}\t|\t{z}\t|\t{miss}\t  |\t{round(relative_miss_min*100,2)}\t\t|")
	print("=========================================================================================================")


def fermats_theorem():
    ## user input input of power and limit of x and y from user and claculate value using near_misses method call

    n = int(input("Enter Exponent value of x and y: "))
    while(n<3 or n>11):
        # check if n is bigger than 2
        print("Value should be bigger than 2 and smaller than 12.")
        n = int(input("Re-Enter Exponent value: "))

    k = int(input("Enter Limit value of x and y: "))
    while(k<11):
        # check if k is bigger than 10
        print("Limit value should be bigger than 10.")
        k = int(input("Re-Enter Limit value: "))

    near_misses(n,k)
    exit = input("Prees any key to exit...")
        
if __name__ == "__main__":
    fermats_theorem()