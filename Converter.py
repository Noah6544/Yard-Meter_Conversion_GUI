from  tkinter import *
root = Tk()

conversion = 1.0936133
def calculateyards():
    global yardinput
    Result = Label(text=str(float(yardinput.get()) / conversion) + " meters", bg="black", fg="white")
    Result.grid(row=3,column=0)

def calculatemeters():
    global meterinput
    meterResult = Label(text=str(float(meterinput.get()) * conversion) + " yards", bg="black", fg="white")
    meterResult.grid(row=3,column=1)


yardinput = Entry(root, width="50", borderwidth="5")
meterinput = Entry(root,width="50",borderwidth="5")
YardDescription_Label = Label(root, text="Calculates Meters from YARDS.\nENTER YARDS", bg = "black",fg="white")
MeterDescription_Label = Label(root, text="Calculates Yards from METERS.\nENTER METERS", bg = "black",fg="white")
yardbutton = Button(root, text="Calculate YARDS", padx="200", pady="50", fg="white", bg="black", command=calculateyards,borderwidth="5")
meterbutton = Button(root, text="Calculate METERS", padx="200", pady="50", fg="white", bg="black", command=calculatemeters, borderwidth="5")

#PACKING
YardDescription_Label.grid(row=0,column=0)
MeterDescription_Label.grid(row=0,column=1)
yardinput.grid(row=1,column=0)
yardbutton.grid(row=2,column=0)
meterbutton.grid(row=2,column=1)
meterinput.grid(row=1,column=1)

root.mainloop()
