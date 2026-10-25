marks = [10,70,3,40]
print("original ",marks)
marks.append(50)# add a new data to the last index
print("added value",marks)
marks.sort()# arranges the data in increasing way
print("arrenged value",marks)
marks.sort(reverse = True)#barranges in decreasing way
print("reverse arrenged ",marks)
marks.reverse()# reverse the whole original data
print("reverse of original ",marks)
marks.insert(2,100)# insert data at a particulor/given index
print("inserted data ",marks)
marks.remove(100)# used  to remove given data
print("after removal ",marks)
marks.pop(2)# removes a given index 
print("after pop ",marks)