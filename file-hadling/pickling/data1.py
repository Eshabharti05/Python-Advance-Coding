with open('E:\\python scripts\\file-hadling\\pickling\pickling.pkl','wb') as f:
    data='the toss is heads','the paper is set c'
    import pickle
    bo=pickle.dumps(data)
    f.write(bo)
    
    
with open('E:\\python scripts\\file-hadling\\pickling\pickling.pkl','wb') as f:
    d={'name':'charan','age':'22'}
    import pickle
    bo=pickle.dump(d,f)

with open('E:\\python scripts\\file-hadling\\pickling\pickling.pkl','rb') as fl:
    import pickle
    bo=fl.read()
    # print(bo)
    # po=pickle.loads(bo)
    # print(po)
    
with open('E:\\python scripts\\file-hadling\\pickling\pickling.pkl','rb') as fl:
    import pickle
    po=pickle.load(fl)
    print(po)
    
    