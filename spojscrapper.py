import requests,bs4
from tkinter import messagebox as tkMessageBox
import tkinter as tk
from tkinter import *
import os


def knowmorefn():
    tkMessageBox.showinfo( "know more", "Sunny Mazumder , undergrad@NIT-silchar.\n www.facebook.com/moovon\n moovonsunny.appspot.com \n moovonjkm@gmail.com \n Feel Free to contact me\n (Thank You for using SpojScrap)")

def openInstruktion():
    os.system('start "" documentation.txt')

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.grid(padx=5, pady=5)
        self.createWidgets()



    def createWidgets(self):
        self.grid()
        label = tk.Label(self,anchor="w",fg="white",bg="#558b2f",text="Enter username : ",padx="65",)
        label.grid(column=0,row=0,columnspan=1,sticky='EW')
        
        self.entry = tk.Entry(self)
        self.entry.grid(column=1,row=0,sticky='EW',padx="5")
        self.entry.bind("<Return>", self.OnPressEnter)

        button = tk.Button(self,anchor="w",bg="#ff1744",fg="white",text=u"Scrap details!",command=self.OnButtonClick)
        button.grid(column=2,row=0,padx=0)
        self.grid_columnconfigure(0,weight=1)

        fullname=tk.Label(self,anchor="w",fg="white",bg="#2196f3",textvariable = fullnamevar)
        fullname.grid(column=0,row=1,sticky='EW')

        worldrank=tk.Label(self, anchor="w",fg="white",bg="#01579b", textvariable=worldrankvar)
        worldrank.grid(column=0,row=2,sticky='EW')

        problemssolved=tk.Label(self, anchor="w",fg="white",bg="#2196f3", textvariable=problemssolvedvar)
        problemssolved.grid(column=0,row=3,sticky='EW')

        solutionssubmitted=tk.Label(self, anchor="w",fg="white",bg="#283593", textvariable=solutionssubmittedvar)
        solutionssubmitted.grid(column=0,row=4,sticky='EW')

        credit1=tk.Label(self, anchor="w",fg="#757575",textvariable=credit1var)
        credit1.grid(column=0,row=7,sticky='EW')

        #credit2=tk.Label(self, anchor="w",fg="#757575",textvariable=credit2var)
        #credit2.grid(column=1,row=7,sticky='EW')

        credit3=tk.Label(self, anchor="w",fg="#757575",textvariable=credit3var)
        credit3.grid(column=0,row=8,sticky='EW')

        credit4=tk.Label(self, anchor="w",fg="#757575",textvariable=credit4var)
        credit4.grid(column=1,row=8,sticky='EW')

        knowmore = tk.Button(self,anchor="w",fg="#757575",activebackground="#76ff03",relief="raised",text=u"know more",command=knowmorefn)
        knowmore.grid(column=1,row=8,padx=0)
        self.grid_columnconfigure(0,weight=1)


        instruktionBtn = Button(self, text='Documentation', command=openInstruktion)
        instruktionBtn.grid(column=2,row=8)

        #fullname.place(x=20,y=20,anchor="w")
    def OnPressEnter(self,event):
        username=self.entry.get()
        r=requests.get("http://www.spoj.com/users/"+username+"/")
        data=r.text 
        soup=bs4.BeautifulSoup(data,"html.parser")
        
        fullnamex="not provided by user"
        userdetails=soup.find('div', {'class':'col-md-3'})
        try:
            for name in userdetails.find_all('h3'):
                fullnamex=name.text
        except Exception:
            pass
        fullnamevar.set("  Fullname : "+fullnamex)




        worldrankx=""
        flag=-1
        try:
            for rankandpoints in userdetails.find_all('p'):
                flag+=1
                if flag==2:
                    #print("  "+rankandpoints.text+"\n")
                    worldrankx=rankandpoints.text
        except Exception:
            pass
        worldrankvar.set(" "+worldrankx)




        link=soup.find_all('dl',{'class':'dl-horizontal profile-info-data profile-info-data-stats'})
        problemssolvedx="invalid username"
        solutionssubmittedx=""
        f=0
        xx=""
        yy=""
        for item in link:   
            problemssolvedx=item.text
        for item in problemssolvedx:
            if problemssolvedx=="invalid username":
                problemssolvedvar.set('  Problems solved ')
                solutionssubmittedvar.set('  Solutions submitted ')
                fullnamevar.set('  Fullname : ')
                worldrankvar.set('  World Rank: ')
                #problemssolvedvar.set(problemssolvedx)
                tkMessageBox.showerror("invalid username", "Please enter a valid user-name\n (It is case-sensitive)")
                #fullnamevar.set('  Fullname : ')
                
                break
            if item=='\n':
                #print(" ",end=' ')
                if f==1:
                    yy+=" "
                if f==0:
                    xx+=" "
            elif item=='d':
                #print("d by  "+username+": ",end='')
                if f==0:
                    xx+="d by  "+username+": "
                if f==1:
                    yy+="d by  "+username+": "

            elif item=='S':
                f=1
                #print('\n')
                #print(" ",end='  ')
                #xx+=item
                yy+=item
                #print(item,end='')
            else:
                #print(item,end='')
                if f==0:
                    xx+=item
                if f==1:
                    yy+=item
        if xx!="":
            problemssolvedvar.set(xx)
        if yy!="":
            solutionssubmittedvar.set("  "+yy)
        #print(xx)
        #print(yy)
        #print(s)
        #os.system(s)
    def OnButtonClick(self):
        username=self.entry.get()
        r=requests.get("http://www.spoj.com/users/"+username+"/")
        data=r.text 
        soup=bs4.BeautifulSoup(data,"html.parser")
        
        fullnamex="not provided by user"
        userdetails=soup.find('div', {'class':'col-md-3'})
        try:
            for name in userdetails.find_all('h3'):
                fullnamex=name.text
        except Exception:
            pass
        fullnamevar.set("  Fullname : "+fullnamex)




        worldrankx=""
        flag=-1
        try:
            for rankandpoints in userdetails.find_all('p'):
                flag+=1
                if flag==2:
                    #print("  "+rankandpoints.text+"\n")
                    worldrankx=rankandpoints.text
        except Exception:
            pass
        worldrankvar.set(" "+worldrankx)




        link=soup.find_all('dl',{'class':'dl-horizontal profile-info-data profile-info-data-stats'})
        problemssolvedx="invalid username"
        solutionssubmittedx=""
        f=0
        xx=""
        yy=""
        for item in link:   
            problemssolvedx=item.text
        for item in problemssolvedx:
            if problemssolvedx=="invalid username":
                problemssolvedvar.set('  Problems solved ')
                solutionssubmittedvar.set('  Solutions submitted ')
                fullnamevar.set('  Fullname : ')
                worldrankvar.set('  World Rank: ')
                #problemssolvedvar.set(problemssolvedx)
                tkMessageBox.showerror("invalid username", "Please enter a valid user-name\n (It is case-sensitive)")
                #fullnamevar.set('  Fullname : ')
                
                break
            if item=='\n':
                #print(" ",end=' ')
                if f==1:
                    yy+=" "
                if f==0:
                    xx+=" "
            elif item=='d':
                #print("d by  "+username+": ",end='')
                if f==0:
                    xx+="d by  "+username+": "
                if f==1:
                    yy+="d by  "+username+": "

            elif item=='S':
                f=1
                #print('\n')
                #print(" ",end='  ')
                #xx+=item
                yy+=item
                #print(item,end='')
            else:
                #print(item,end='')
                if f==0:
                    xx+=item
                if f==1:
                    yy+=item
        if xx!="":
            problemssolvedvar.set(xx)
        if yy!="":
            solutionssubmittedvar.set("  "+yy)





jkm = tk.Tk()
jkm.geometry("440x150")
jkm.resizable(width=FALSE, height=FALSE)
jkm.wm_iconbitmap('icona.ico')

fullnamevar = StringVar()
worldrankvar=StringVar()
problemssolvedvar=StringVar()
solutionssubmittedvar=StringVar()
credit1var=StringVar()
credit2var=StringVar()
credit3var=StringVar()
credit4var=StringVar()
problemssolvedvar.set('  Problems solved ')
solutionssubmittedvar.set('  Solutions submitted ')
fullnamevar.set('  Fullname : ')
worldrankvar.set('  World Rank: ')
credit3var.set('SpojScrap v4 -   www.github.com/moovon ')
#credit4var.set('moovonjkm@gmail.com')
credit1var.set('-----------------------------------------------------')
app = Application(master=jkm)

app.master.title(" Spoj Scrapper v4.0")
app.mainloop()