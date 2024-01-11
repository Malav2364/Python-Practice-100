#methods in dictionary

ep = {
    122: 45,
    123: 50,
    124: 60,
    125: 60,
    126: 69,
}

ep2 = {
    222: 67,
    566: 70,
}

ep.update(ep2) #here we merged the ep2 dict with ep
# print(ep)#print the combined ep's
# ep.clear()#here we cleared the dictionary using clear method
ep.pop(122) #to remove first element form the dictionary
ep.popitem()#to remove last element from the dictionary
del ep2#to delete the whole dictionary with the data 
del ep[125]#to delete whole entry i.e, key and value both
print(ep)

