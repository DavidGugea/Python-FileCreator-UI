import tkinter, sys, random, pickle
root = tkinter.Tk()

class Project:
    def __init__(self, master):
        self.master = master 
        
        # Make a text widget // adding a scrollbar to it 
        self.textWidget = tkinter.Text(self.master, width=100, height=15, bg="#FFFFFF", bd=10, relief="flat", font=('Arial', 10))
        self.scroll = tkinter.Scrollbar(self.master, orient="vertical")
        self.scroll.configure(command=self.textWidget.yview)
        self.textWidget.configure(yscrollcommand=self.scroll)
        self.textWidget.pack(side="left")
        self.scroll.pack(side="left", fill="y")
        
        self.mSave_CONTEXT = tkinter.Menu(self.master)
        self.textWidget.bind("<Button 3>", self.pop_CONTEXT)
        self.mSave_CONTEXT.configure(tearoff=0)
        self.mSave_CONTEXT.add_command(label="Save", command=self.SAVE_BY)
        self.fTYPE_var = tkinter.StringVar()
        self.fTYPE_var.set(".txt")
        
        self.mSave_CONTEXT.add_checkbutton(label="Text File(.txt)", onvalue=".txt", offvalue=".txt", variable=self.fTYPE_var)
        self.mSave_CONTEXT.add_checkbutton(label="Html File(.html)", onvalue=".html", offvalue=".txt", variable=self.fTYPE_var)
        self.mSave_CONTEXT.add_checkbutton(label="Css File(.css)", onvalue=".css", offvalue=".txt", variable=self.fTYPE_var)
        self.mSave_CONTEXT.add_checkbutton(label="Python File(.py)", onvalue=".py", offvalue=".txt", variable=self.fTYPE_var)
        self.mSave_CONTEXT.add_checkbutton(label="Binary File(.bin)", onvalue=".bin", offvalue=".txt", variable=self.fTYPE_var)

        self.mainMenu = tkinter.Menu(self.master)
        self.mConfigure = tkinter.Menu(self.mainMenu)
        self.mConfigure.configure(tearoff=1)
        
        self.colorVar = tkinter.StringVar()
        self.colorVar.set("#FFFFFF")
        self.reliefVar = tkinter.StringVar()
        self.reliefVar.set("flat")

        self.mConfigure.add_radiobutton(label="Red", value="#FF0000", variable=self.colorVar, command=self.change_BG)
        self.mConfigure.add_radiobutton(label="Blue", value="#0000FF", variable=self.colorVar, command=self.change_BG)
        self.mConfigure.add_radiobutton(label="Green", value="#00FF00", variable=self.colorVar, command=self.change_BG)
        self.mConfigure.add_radiobutton(label="White", value="#FFFFFF", variable=self.colorVar, command=self.change_BG)
        self.mConfigure.add_radiobutton(label="Black", value="#000000", variable=self.colorVar, command=self.change_BG) 
        self.mConfigure.add_separator()
        self.mConfigure.add_radiobutton(label="Flat Relief", value="flat", variable=self.reliefVar, command=self.add_Relief)
        self.mConfigure.add_radiobutton(label="Groove Relief", value="groove", variable=self.reliefVar, command=self.add_Relief)
        self.mConfigure.add_radiobutton(label="Raised Relief", value="raised", variable=self.reliefVar, command=self.add_Relief)
        self.mConfigure.add_radiobutton(label="Sunken Relief", value="sunken", variable=self.reliefVar, command=self.add_Relief)
        
        self.mWidget = tkinter.Menu(self.mainMenu)
            
        self.mWidget.add_command(label="Increase Widget Width", command=self.increase_WidgetWidth)
        self.mWidget.add_command(label="Decrease Widget Width", command=self.decrease_WidgetWidth)
        self.mWidget.add_command(label="Increase Widget Height", command=self.increase_WidgetHeight)
        self.mWidget.add_command(label="Decrease Widget Height", command=self.decrease_WidgetHeight)
        
        self.mFont = tkinter.Menu(self.mainMenu)
        self.mFont.configure(tearoff=1)

        self.FG_VAR = tkinter.StringVar()
        self.FG_VAR.set("black")
        self.FONT_VAR = tkinter.StringVar()
        self.FONT_VAR.set("Arial")
        
        self.mFont.add_command(label="Increase Font", command=self.increaseFont)
        self.mFont.add_command(label="Decrease Font", command=self.decreaseFont)
        self.mFont.add_separator()
        self.mFont.add_checkbutton(label="Red FG", onvalue="red", offvalue="black", variable=self.FG_VAR, command=self.change_FG)
        self.mFont.add_checkbutton(label="Blue FG", onvalue="blue", offvalue="black", variable=self.FG_VAR, command=self.change_FG)
        self.mFont.add_checkbutton(label="Yellow FG", onvalue="yellow", offvalue="black", variable=self.FG_VAR, command=self.change_FG)
        self.mFont.add_checkbutton(label="Black FG", onvalue="black", offvalue="black", variable=self.FG_VAR, command=self.change_FG)
        self.mFont.add_checkbutton(label="White FG", onvalue="white", offvalue="black", variable=self.FG_VAR, command=self.change_FG)
        self.mFont.add_separator()
        self.mFont.add_radiobutton(label="Arial", command=self.change_Font, variable=self.FONT_VAR, value="Arial")
        self.mFont.add_radiobutton(label="Times", command=self.change_Font, variable=self.FONT_VAR, value="Times")
        self.mFont.add_radiobutton(label="Courier", command=self.change_Font, variable=self.FONT_VAR, value="Courier")
        self.mFont.add_radiobutton(label="Consolas", command=self.change_Font, variable=self.FONT_VAR, value="Consolas")
        self.mFont.add_radiobutton(label="Bahnschrift", command=self.change_Font, variable=self.FONT_VAR, value="Bahnschrift")
        self.mainMenu.add_cascade(label="Font", menu=self.mFont)
        self.mainMenu.add_cascade(label="Widget", menu=self.mWidget)
        self.mainMenu.add_cascade(label="Configure", menu=self.mConfigure)
        self.master["menu"] = self.mainMenu
    def increaseFont(self):
        myFont = self.textWidget["font"].split(" ")
        myFont[1] = int(myFont[1])
        myFont[1] += 2
        self.textWidget["font"] = myFont 
    def decreaseFont(self):
        myFont = self.textWidget["font"].split(" ")
        myFont[1] =  int(myFont[1])
        myFont[1] -= 2
        self.textWidget["font"] = myFont 
    def change_FG(self):
        self.textWidget["fg"] = self.FG_VAR.get()
    def change_Font(self):
        myFont = self.textWidget["font"].split(" ")
        myFont[0] = self.FONT_VAR.get()
        self.textWidget["font"] = myFont
    def increase_WidgetWidth(self):
        self.mWidget["width"] += 3
    def decrease_WidgetWidth(self):
        self.mWidget["width"] -= 3
    def increase_WidgetHeight(self):
        self.mWidget["height"] += 3
    def decrease_WidgetHeight(self):
        self.mWidget["height"] -= 3
    def change_BG(self):
        self.textWidget["bg"] = self.colorVar.get()
    def add_Relief(self):
        self.textWidget["relief"] = self.reliefVar.get()
    def pop_CONTEXT(self, KOO):
        self.mSave_CONTEXT.tk_popup(KOO.x_root, KOO.y_root)
        # KOO = coordinates
    def SAVE_BY(self):
        self.saveText = self.textWidget.get("1.0", "end")
        RN = int(random.randint(1, 101))
        if self.fTYPE_var.get() == ".bin":
            #Binary file 
            dfile = open("BinaryFile{0}.bin".format(RN), "wb")
            # wb // write binary 
            pickle.dump(self.saveText, dfile)
            dfile.close()
        else:
            dfile = open("File{0}{1}".format(RN, self.fTYPE_var.get()), "w")
            dfile.write("{0}".format(self.saveText))
            dfile.close()
project = Project(root)
root.mainloop()
