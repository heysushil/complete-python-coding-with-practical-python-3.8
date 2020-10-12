# read current file
userfilename = open('file_handling/demo/sushil.txt', 'r')
# get number of char
# readdata = userfilename.read(5)

# readline using readline()
# readdata = userfilename.readline()

readdata = userfilename.readlines()

print('\n', readdata)
print('\n', readdata[0])
userfilename.close()