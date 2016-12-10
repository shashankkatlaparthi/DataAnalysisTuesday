#!/usr/bin/python
import one, two, three, four, five
import Tkinter

'''
one.analysis_one()
two.analysis_two()
three.analysis_three()
four.analysis_four()
'''

class client_gui(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.display_text = "Welcome to Movie Analysis"
        #self.app_running = True
        self.initialize()
        

    def initialize(self):
        self.grid()

        self.analysis_two_text = """Enter the genre number to be plotted:
1  :  Action            2  :  Adventure
3  :  Animation         4  :  Biography
5  :  Comedy            6  :  Crime
7  :  Documentary       8  :  Drama
9  :  Family            10  :  Fantasy
11  :  Film-Noir        12  :  History
13  :  Horror           14  :  Music
15  :  Musical          16  :  Mystery
17  :  News             18  :  Romance
19  :  Sci-Fi           20  :  Short
21  :  Sport            22  :  Thriller
23  :  War              24  :  Western"""
        
        # Button 1
        button = Tkinter.Button(self,text=u"Analysis 1",
            command=self.analysis_one)
        button.grid(column=0,row=1,sticky='EW')

        # Button 1
        button = Tkinter.Button(self,text=u"Analysis 2",
            command=self.analysis_two)
        button.grid(column=0,row=2,sticky='EW')

        # Button 1
        button = Tkinter.Button(self,text=u"Analysis 3",
            command=self.analysis_three)
        button.grid(column=0,row=3,sticky='EW')

        # Button 1
        button = Tkinter.Button(self,text=u"Analysis 4",
            command=self.analysis_four)
        button.grid(column=0,row=4,sticky='EW')

        # Button 1
        button = Tkinter.Button(self,text=u"Analysis 5",
            command=self.analysis_five)
        button.grid(column=0,row=5,sticky='EW')

       
        
    def analysis_one(self):
    	one.analysis_one()

    def analysis_two(self):
        
        # Enter Text Field
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid(column=2,row=0,sticky='EW')
        self.entry.bind("<Return>", self.second_analysis)
        self.entryVariable.set(u"")
        
        # Display Field
        self.displayVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.displayVariable,
            anchor="sw",fg="white",bg="blue",height=13,width=30,justify="left")
        label.grid(column=1,row=0,columnspan=1,rowspan=30,sticky='EW')
        self.displayVariable.set(u"")
        
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        
    	self.update_display(self.analysis_two_text)
    	self.entryVariable.set(u"Enter number here.")
    	self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def analysis_three(self):
    	three.analysis_three()

    def analysis_four(self):
    	four.analysis_four()

    def analysis_five(self):
    	five.analysis_five()


    '''
    def recv(self):
        while self.app_running:
            data, a = self.s.recvfrom(1024)
            if data:
                self.display_text = self.display_text + "\n" + data
                self.update_display()
    def on_closing(self):
        pdb.set_trace()
        self.app_running = False
        self.s.close()
        self.destroy()
        sys.exit()'''

    def second_analysis(self,event = 0):
        two.analysis_two(self.entryVariable.get())


    def update_display(self,text):
        self.displayVariable.set(text)



if __name__ == "__main__":
    app = client_gui(None)
    #app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
    