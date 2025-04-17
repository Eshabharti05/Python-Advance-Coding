#converting user-defined data into json format of data usiing dumps function
with open('E:\\python scripts\\file-hadling\\Json\jsondata1.txt','w') as file:
    import json
    po={'name':'ad','male':True,'female':False,'gf':None,'phone':(123,456)}
    print(po)
    jo=json.dumps(po)
    print(jo)
    file.write(jo)
    #converted python object into jso and created a file with name jsondata1.txt
##################################################################################
#converting user-defined data into json format of data usiing dump function
with open('E:\\python scripts\\file-hadling\\Json\jsondata2.txt','w') as file:
    import json
    po={'name':'charan','male':True,'female':False,'gf':None,'phone':(898989898)}
    print(po)
    jo=json.dump(po,file)
    print(jo)
#converted python object into jso and created a file with name jsondata2.txt
###########################################################################################
#reading the json data and re-converting into python object using loads function
with open('E:\\python scripts\\file-hadling\\Json\jsondata1.txt','r') as file:
    import json
    jo=file.read()
    print(jo)
    po=json.loads(jo)
    print(po)
####################################################################################################
#reading the json data and re-converting into python object using loads function
with open('E:\\python scripts\\file-hadling\\Json\jsondata2.txt','r') as file:
    import json
    # print(file)
    po=json.load(file)
    print(po)