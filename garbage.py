import sys
import datetime as dt
from random import choice
from string import ascii_lowercase

def main():
	start = dt.datetime.now()
	try:
		outFile = open("Output.txt", "w")
		maxLen = int(sys.argv[1])*1000
		percAvg = 0
		for x in range(maxLen):
			percAvg = 100.0*(x/maxLen)
			print("[{0:.2f}%]".format(percAvg))
			outFile.write(choice(ascii_lowercase))
		
	except:
		raise Exception("Error generating file!")
	finally:
		outFile.close()
		end = dt.datetime.now()
		print("[100%]\n")
		print("Garbage Generation Complete!\n")
		print("\nTotal Execution Time: {}".format(end-start))


if __name__ == "__main__":
	main()
