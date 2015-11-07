import sys

def parseFile(file):
	print(file)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Improper number of arguments.")
	else:
		parseFile(sys.argv[1])