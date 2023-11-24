# Recursively print all subclasses of a given exception class
def printExceptionsTree(exceptionClass, level=0):
    if level > 1:
        print("   |" * (level - 1), end="")
    if level > 0:
        print("   +---", end="")
    print(exceptionClass.__name__)

    # Base case: no more subclasses
    for subclass in exceptionClass.__subclasses__():
        # Recursive case: print sub-tree of this subclass
        printExceptionsTree(subclass, level + 1)

# printExceptionsTree(BaseException)
printExceptionsTree(OSError)