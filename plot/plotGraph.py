import matplotlib.pyplot  as plt

a = ['bhadresh', 'suresh', 'mahesh', 'kamlesh', 'jignesh']
b = [25, 20, 21, 23, 18]
plt.plot(a,b, 'r')
plt.ylabel('Age', fontsize=15)
plt.xlabel('Names', fontsize=15)
plt.title('Ages of Group A', fontsize=20)
plt.grid(True)
plt.minorticks_on()
plt.show()                         

#empty figure
# fig = plt.figure() #empty figure BLANK
# fig, ax = plt.subplots()#empty graph with axis on it
# fig, axes = plt.subplots(2,2)#2 by 2 empty graphs with axis ofc
# fig, axes = plt.subplot_mosaic([['left_top', 'right'], ['left_bottom', 'right']]) #here we are giving postition like one with "TOP" & "BOTTOM" will be divided into two graphs other will be SINGLE
# plt.show()