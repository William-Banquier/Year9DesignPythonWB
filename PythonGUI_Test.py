import tkinter as tk



def calcVolumeCylinder(radius, height):
	import math as m
	print("Volume Of A Cylinder Formula")
	volume = round((height*(radius**2))*m.pi, 2)
	print("The Volume Is",volume)


def runMe():
	volume = calcVolumeCylinder(3,4)
	#print(volume)

#Main Code:
root = tk.Tk()
#Building widgets goes before mainloop.
title = tk.Label(root, text = "Cylinder Volume Calculator")
title.config(fg = "red", bg = "black")
title.pack(fill = tk.BOTH)

radiusLabel = tk.Label(root, text = "Radius:")
radiusLabel.config(anchor = tk.W)
radiusLabel.pack(fill = tk.BOTH)

radiusEntry = tk.Entry(root)
radiusEntry.config()
radiusEntry.pack(fill = tk.BOTH)

heightEntry = tk.Entry(root)
heightEntry.config()
heightEntry.pack(fill = tk.BOTH)

heightLabel = tk.Label(root, text = "Height:")
heightLabel.config(anchor = tk.W)
heightLabel.pack(fill = tk.BOTH)

output = tk.Text(root)
output.config(width = 50, height = 10,state = "disabled",borderwidth = 2,relief = "groove")
output.pack()


btnrun = tk.Button(root, text = "CALCULATE", highlightbackground='#3E4149')
btnrun.config(fg="blue",command = runMe)
btnrun.pack(fill = tk.BOTH)

check = tk.Checkbutton(root, text = "High Contrast")
check.config(anchor = tk.W)
check.pack(fill = tk.BOTH)


#varible name   x = tk.("prompt")
# tk type
#configer
#return

root.mainloop()
print("End Program")