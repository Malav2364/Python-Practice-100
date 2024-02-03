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