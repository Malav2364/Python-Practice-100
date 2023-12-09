import time 
name = str(input("Enter your name :"))
strtime = time.strftime("%H")
stime = time.strftime("%I").lstrip("0")
int_time = int(strtime)

if (int_time > 0 and int_time < 12):
    print("Good Morning",name,"it's", stime, "o'clock")
elif(int_time >= 12 and int_time < 17):
    print("Good Afternoon",name,"it's", stime, "o'clock")
elif(int_time >= 17 and int_time < 21):
    print("Good Evening",name,"it's", stime, "o'clock")
else:
    print("Good Night",name,"it's", stime, "o'clock")
