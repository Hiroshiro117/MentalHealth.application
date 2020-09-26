import tkinter
from tkinter import messagebox
import webbrowser
import winsound


####################################################################
def mentalHealth_Button():
    inside = tkinter.Tk()
    inside.resizable(False, False)

    # #inside Resource button
    # inside_b2= tkinter.Button(inside, text ="List Resources by HighSchool", command = chatBox, fg="black", bg = "light gray")
    # inside_b2.pack()
    # inside_b2.place(x = 90, y = 110, height = 27, width = 180)
    
    ####
    highschoolMenu=  tkinter.Menubutton ( inside, text="List Resources by Highschool" )
    highschoolMenu.grid()
    highschoolMenu.menu =  tkinter.Menu ( highschoolMenu, tearoff = 0 )
    highschoolMenu["menu"] =  highschoolMenu.menu


    highschoolMenu.menu.add_checkbutton ( label="Clairemont High School", command = lambda: tkinter.messagebox.showinfo("Clairemont High", "(619) 605-2600, https://www.sandiegounified.org/schools/clairemont/counseling-appointment-request"))
    highschoolMenu.menu.add_checkbutton ( label="Crawford High School", command = lambda: tkinter.messagebox.showinfo("Crawford High", "(619) 362-3700, https://www.sandiegounified.org/schools/crawford/contact-us"))
    highschoolMenu.menu.add_checkbutton ( label="Henry High School", command = lambda: tkinter.messagebox.showinfo("Henry High", "(619) 286-7700, https://patrickhenryhs.net/counseling"))
    highschoolMenu.menu.add_checkbutton ( label="Hoover High School", command = lambda: tkinter.messagebox.showinfo("Hoover High", "(619) 344-4500, https://www.sandiegounified.org/schools/hoover/counseling-overview"))

    highschoolMenu.pack()
    highschoolMenu.place(x = 95, y= 120, height = 30, width = 180)
    ###

    ### COLLEGES ###
    collegeMenu=  tkinter.Menubutton ( inside, text="List Resources by College" )
    collegeMenu.grid()
    collegeMenu.menu =  tkinter.Menu (collegeMenu, tearoff = 0 )
    collegeMenu["menu"] =  collegeMenu.menu

    collegeMenu.menu.add_checkbutton ( label="California State University - San Marcos", command = lambda: tkinter.messagebox.showinfo("CSUSM", "(760)-750-4000, https://www.psychologytoday.com/us/therapists/91941/66016?sid=5e598f1979e96&ref=1&tr=ResultsName"))
    collegeMenu.menu.add_checkbutton ( label="San Diego State University", command = lambda: tkinter.messagebox.showinfo("SDSU", "(619)-594-5200, https://svcrplv.uhc.com/sdchat/"))
    collegeMenu.menu.add_checkbutton ( label="University of California San Diego", command = lambda: tkinter.messagebox.showinfo("UCSD", "(858)-534-2230, https://wellness.ucsd.edu/caps/Pages/default.aspx"))
    collegeMenu.menu.add_checkbutton ( label="Point Loma Nazarene University", command = lambda: tkinter.messagebox.showinfo("PLNU", "(619)-849-2200, https://up2sd.org/resources/mental-health-local/"))
    
    collegeMenu.pack()
    collegeMenu.place(x = 95, y= 220, height = 30, width = 180)

    # titling mental Health Button
   
    inside.title("Mental Health Awareness")
    inside.geometry('350x400+500+500')

    inside.config(bg="orange red")
    inside.mainloop()




########################################################################


#########################################################################
def chatBox():

    chat=tkinter.Tk()

    def send(event):
        send = "You: "+e.get()
        txt.insert(tkinter.END, "\n"+send)
        if(e.get() == "I'm sad"):
            txt.insert(tkinter.END,"\n"+"Mary (Counselor): Don't worry, I believe in you!")
        elif(e.get() == "School sucks"):
            txt.insert(tkinter.END,"\n"+"Mary (Counselor): I agree, but it'll all be worth it.")
        elif(e.get() == "I need someone to talk to"):
            txt.insert(tkinter.END,"\n"+"Mary (Counselor): I'm right here, how are you?")
        elif(e.get() == "I feel depressed"):
            txt.insert(tkinter.END,"\n"+"Mary (Counselor): I'm sorry :(, it'll all get better I promise you!")
        elif(e.get() == "I'm going to hurt my self"):
            txt.insert(tkinter.END,"\n"+"Mary (Counselor): Help is on the way, please stay with me!")
        else:
            txt.insert(tkinter.END,"\n"+"Mary (Counselor): Please call the national lifeline: 1-800-273-8255")
        e.delete(0,tkinter.END)
    txt=tkinter.Text(chat)
    txt.grid(row=0,column=0,columnspan=2)
    e=tkinter.Entry(chat,width=100)
    e.bind("<Return>", send)
    send=tkinter.Button(chat,text="SEND",command=send).grid(row=1,column=1)
    e.grid(row=1,column=0)


    chat.title("CHAT BOX")
    chat.config(bg="red")
    chat.resizable(False, False)
    chat.mainloop()

    

######################################################################


def links():

    def callback(url):
        webbrowser.open_new(url)

    website = tkinter.Tk()

    # All my links 
    link1 = tkinter.Label(website, text="National Suicide Prevention Lifeline", fg="blue", cursor="hand2", bg = "plum1")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://suicidepreventionlifeline.org/"))
    link1.place(x=5 , y= 10)

    link2 = tkinter.Label(website, text="Crisis Textline", fg="blue", cursor="hand2", bg = "plum1")
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback("https://www.crisistextline.org/"))
    link2.place(x= 5, y= 50)

    link3 = tkinter.Label(website, text="National Alliance on Mental Illness", fg="blue", cursor="hand2", bg= "plum1")
    link3.pack()
    link3.bind("<Button-1>", lambda e: callback("https://www.nami.org/"))
    link3.place(x= 5,y= 90)

    link4 = tkinter.Label(website, text="MentalHealth.gov", fg="blue", cursor="hand2", bg= "plum1")
    link4.pack()
    link4.bind("<Button-1>", lambda e: callback("https://www.mentalhealth.gov/"))
    link4.place(x= 5,y= 130)


    website.resizable(False, False)
    website.title("Helpful Contact Websites")
    website.geometry("400x180")
    website.config(bg = "plum1")
    website.mainloop()
########################################################################


def resources_links():

    def callback(url):
        webbrowser.open_new(url)

    resources = tkinter.Tk()

    # All my resources
    resource1 = tkinter.Label(resources, text="My Depression Team", fg="blue", cursor="hand2", bg = "hot pink")
    resource1.pack()
    resource1.bind("<Button-1>", lambda e: callback("https://www.mydepressionteam.com/"))
    resource1.place(x=140 , y= 10)

    resource2 = tkinter.Label(resources, text="Anxiety and Depression Association of America", fg="blue", cursor="hand2", bg = "hot pink")
    resource2.pack()
    resource2.bind("<Button-1>", lambda e: callback("https://adaa.org/"))
    resource2.place(x=80 , y= 75)

    resource3 = tkinter.Label(resources, text="Online Counseling", fg="blue", cursor="hand2", bg = "hot pink")
    resource3.pack()
    resource3.bind("<Button-1>", lambda e: callback("https://www.talkspace.com/"))
    resource3.place(x=140 , y= 140)

    medicineButton =tkinter.Button(resources, text ="Medications", command = lambda: tkinter.messagebox.showinfo("Medications", "Cymbalta (duloxetine) \nViibryd (vilazodone hydrochloride) \nPristiq (desvenlafaxine) \nCelexa (citalopram) \nWellbutrin (bupropion) "))
    therapyButton =tkinter.Button(resources, text ="Therapy", command = lambda: tkinter.messagebox.showinfo("Therapy", "American Psychological Association \nAnxiety and Depression Association of America \nNational Center for Complimentary and Integrative Health"))

    medicineButton.pack()
    medicineButton.place(x=100, y = 200, height = 30, width = 200)

    therapyButton.pack()
    therapyButton.place(x=100, y = 260, height = 30, width = 200)
    
    resources.resizable(False, False)
    resources.title("Resources and Information")
    resources.geometry("400x320+700+400")
    resources.config(bg = "hot pink")
    resources.mainloop()
#################################################################################

# this creates the main window
top = tkinter.Tk()
top.resizable(False, False)

# titling the application box 
top.title("HEALTH YEA!")
top.geometry('500x500+100+200')
top.config(bg= "cyan")
top.grid()

leftFrame = tkinter.Frame(top, width=500, height = 500, bg="#C8F9C4", highlightthickness=10, highlightbackground="#111")



# creating a button for mental health
b1 =tkinter.Button(top, text ="Mental Health", command = mentalHealth_Button, bg = "light gray", fg="black")
# button for QUIT
b2 =tkinter.Button(top, text ="QUIT", command = top.quit, fg="red", bg = "light gray")
b3 = tkinter.Button(top, text ="Resources", command = resources_links, fg="black", bg = "light gray")
b4 = tkinter.Button(top, text ="Contact", command = links, fg="black", bg = "light gray")
b5 = tkinter.Button(top, text ="Chat", command = chatBox, fg="black", bg = "light gray")



# button placements 
b1.pack(fill = tkinter.X, padx= 10)
b1.place(x = 150, y = 38, height = 30, width = 200)

b2.pack(fill = tkinter.X,side=tkinter.BOTTOM, padx = 5 )
b2.place(x = 50, y = 450, height = 30, width = 400)

b3.pack()
b3.place(x = 150, y= 238, height = 30 , width = 200)

b4.pack()
b4.place(x=150, y = 338, height = 30, width = 200)

b5.pack()
b5.place(x=150, y = 138, height = 30, width = 200)

# play sound
winsound.PlaySound('C:/Users/bashi/Downloads/sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

#add icon image
top.iconbitmap(True, "C:/Users/bashi/Downloads/Treetog-I-Help.ico")

# add image
photo = tkinter.PhotoImage(file= "C:/Users/bashi/Downloads/application2.png")
imagePhoto = tkinter.Label(image=photo)
imagePhoto.image = photo # keep a reference!
imagePhoto.pack()
imagePhoto.place(x=10, y= 10, height = 90, width = 100)



# main loop of my main application
top.mainloop()
