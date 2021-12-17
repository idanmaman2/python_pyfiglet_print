import pyfiglet
from tkinter import *
result = pyfiglet.figlet_format("HELLO", font = "broadway")
res2=pyfiglet.figlet_format("WORLD", font = "broadway")
result1 = pyfiglet.figlet_format("THEY", font = "doh")
res21=pyfiglet.figlet_format("WILL NOTICE", font = "doh")
result2 = pyfiglet.figlet_format("YOU", font = "bigchief")
res22=pyfiglet.figlet_format("  ", font = "bigchief")
result3 = pyfiglet.figlet_format(" ", font = "barbwire")
res23=pyfiglet.figlet_format("", font = "barbwire")
import time

root = Tk()
root.geometry('2200x1800')
T = Text(root, height=300, width=500,bg="black",fg="blue")
T.pack()
quote ='\n\n'+result+'\n\n\n'+res2+'\n\n\n\n'+'\n\n'+result1+'\n\n\n'+res21+'\n\n\n\n\n\n\n\n'+'\n\n'+result2+'\n\n\n'+res22+'\n\n\n\n\n\n\n\n'+'\n\n'+result3+'\n\n\n'+res23+'\n\n\n\n\n\n\n\n'

y1="____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________"
T.insert(END, quote)
root2=Tk()
z=False
z=bool(z)
def new_frequency_1000times(k=0):
    global z 
    b=10
    a=str(0)
    if k < 9000000000:
        if ((k%599)>99):
            a=ord ('a')+int ((k%599)/100)
            a=chr(a)
        print ("#99"+a+"f"+str(k%100+10))
        b=(k%599)%90+10
        b=str(b)
        T.configure(fg="#99"+a+"f"+(b))
        #1000 ms = 1 seconds, adjust to taste.
        root.after(45, lambda: new_frequency_1000times(k+1))
    else:
        if(not(z)):
            root.destroy()
            z=True
        

b=Button(root2,text="start the fun",font="Times 16",fg="green",bg="red",height=2, width=5,command=new_frequency_1000times)
b.pack()
root2.mainloop()


root.mainloop()
