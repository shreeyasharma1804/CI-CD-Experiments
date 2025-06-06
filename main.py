import pickle

def add(a,b):
    return a+b

def create_object():
    number = add(4,5)
    return {"number": number}

def serilaze_object():
    obj = create_object()
    pickle.dump(obj, open("object.pkl", "wb"))
    
def deserialize_object():
    obj = pickle.load(open("object.pkl", "rb"))
    print(obj)