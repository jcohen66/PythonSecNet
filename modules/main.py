# from my_functions import message
# from my_functions import *
from my_functions import message as my_message

def main():
    # with import my_functions
    # my_functions.message('Python')

    # with from my_functions import message
    # message('Python')

    # with from my_functions import message as my_message
    my_message('Python')

if __name__ == "__main__":
    main()