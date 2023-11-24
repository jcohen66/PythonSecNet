try:
    myfile = open('newfile.txt', 'wt')
    for i in range(10):
        myfile.write(f'Line #: {(i+1)}\n')
    myfile.close()
except IOError as error:
    print("I/O error occurred: ", str(error.errno))
