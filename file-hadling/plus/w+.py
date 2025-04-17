with open('E:\\python scripts\\file-hadling\\plus\\filedata.txt','w+') as f:
    f.write('excuse me sir')
    f.seek(0)
    print(f.read())
    #output=excuse me sir
    #here using w+ mode we can write in the file then use seek method and red it from the specific index position
    '''but we cannot read first and write next as every time when i open a file using write mode the file is created
    if not there and the file data is deleted if the file is already existing'''
##############''e+''mode also works the same as w+ mode ##############
########################################################################################
with open('E:\\python scripts\\file-hadling\\plus\\filedata.txt','a+') as f:
    # print(f.read()) no output because the cursor is at the end of the file as it is in append mode soooo seek first
    f.seek(0)
    print(f.read())  #o/p:- excuse me sir
    f.write(' may i')
    f.seek(0)
    print(f.read())  #o/p:- excuse me sir may i
#so here we can also read first and can write next as data is added at the end, not inserted any where between irrespective of the cursor position
###############
with open('E:\\python scripts\\file-hadling\\plus\\filedata.txt','a+') as f:
    f.write(' come in')
    f.seek(0)
    print(f.read()) #o/p:-excuse me sir may i come in
#so here we can also write first and can read next
#########################################################################################
#by using r+ also both read and write operations can be performed
with open('E:\\python scripts\\file-hadling\\plus\\filedata.txt','r+') as f:
    f.write('hello madam') #only here in r+ the data has the ability to get overwritten by the text u write
    f.seek(0)
    print(f.read()) #output:-hello madamir may i come in 
#here also we can overwrite the data and read next and vice versa is also possible as the cursor is at the begining 
    

    