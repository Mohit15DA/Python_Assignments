"""
BINARY FILE:

Question:
How to write data in a file.

Solution:
import pickle
file= open ('employee.bin','wb')
# pickle.dump('data','file_handler')
pickle.dump('Anupam',file)
file.close()


Question:
How to read data in a file.

Solution:
import pickle
file= open ('employee.bin','rb')
# pickle.load('file_handler')
try:
    while True:
        data= pickle.load(file)
        print(data)
except:
    print("Read successfully")
file.close()




"""
