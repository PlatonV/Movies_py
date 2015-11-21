RED = '\033[91m'
GREEN = '\033[92m'
BOLD = '\033[1m'
END = '\033[0m'

def custom_assert(assertionString, condition):
    print("Testing: " + assertionString)
    if condition:
        print(GREEN + "SUCCES!" + END)
    else:
        print(RED + "FAILURE!" + END)
