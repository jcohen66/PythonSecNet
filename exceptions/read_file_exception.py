try:
    file_handle = open("myfile.txt", "r")
except IOError as error:
    print("I/O error occurred: ", str(error.errno))
except Exception as exception:
    print("Unexpected error occurred: ", str(exception))
else:
    print("File opened successfully")
    file_handle.close()
    