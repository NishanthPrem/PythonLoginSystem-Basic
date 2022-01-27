# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:52:34 2019

@author: Nishanth
"""

from tkinter import *
import os

def destroy_screen5():
    screen5.destroy()

def saved():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("Info")
    screen5.geometry("100x100")
    
    Label(screen5,text="").pack()
    Button(screen5,text="Saved",command=destroy_screen5).pack()

def create_file():
    file_name=cn_file.get()
    text1=cn_text.get()
    
    data=open(file_name,"w")
    data.write(text1)
    data.close()
    saved()

def del_func():
    
    del1=delete_file.get()
    
    if os.path.exists(del1):
        os.remove(del1)
        Label(screen6,"Deleted Successfully",bg="green").pack()
        
    else:
        Label(screen6,"File doesnt exist",bg="red").pack()
        
def view_func():
    
    view1=view_var.get()
    if os.path.exists(view1):
        file=open(view1,"r")
        dataq=file.read().splitlines()
        screen8=Toplevel(screen)
        screen8.geometry("400x400")
        Label(screen8,text=dataq).pack()
    else:
        Label(screen7,"File doesnt exist",bg="red").pack()
    

def create_note():
    global cn_file
    global cn_file_entry
    global cn_text
    global cn_text_entry
    
    screen4=Toplevel(screen)
    screen4.title("Create Notes")
    screen4.geometry("400x400")
    
    cn_file=StringVar()
    cn_text=StringVar()
    
    Label(screen4,text="Enter a file name").pack()
    cn_file_entry=Entry(screen4,textvariable=cn_file).pack()
    Label(screen4,text="Enter text").pack()
    cn_text_entry=Entry(screen4,textvariable=cn_text).pack()
    Label(screen4,text="").pack()
    Button(screen4,text="Create File",command=create_file).pack()
    

def view_note():
    global view_var
    
    screen7=Toplevel(screen)
    screen7.title("Notes")
    screen7.geometry("400x400")
    
    view_var=StringVar()
    
    Label(screen7,text="Enter a file name").pack()
    view_entry=Entry(screen7,textvariable=view_var)
    view_entry.pack()
    Label(screen7,text="").pack()
    Button(screen7,text="View",command=view_func).pack()
    
    

def delete_note():
    
    global delete_file
    global df_entry
    global screen6
    
    screen6=Toplevel(screen)
    screen6.title("Delete File")
    screen6.geometry("400x400")
    
    delete_file=StringVar()
    
    Label(screen6,text="Enter File to be deleted").pack()
    Label(screen6,text="").pack()
    df_entry=Entry(screen6,textvariable=delete_file)
    df_entry.pack()
    Label(screen6,text="").pack()
    Button(screen6,text="Delete!",command=del_func).pack()
    
def notes():
    screen3=Toplevel(screen)
    screen3.title("Notes")
    screen3.geometry("400x400")
    
    Label(screen3,text="Welcome to the dashboard",bg="grey",width="300").pack()
    Label(screen3,text="").pack()
    Button(screen3,text="Create Note",command=create_note).pack()
    Label(screen3,text="").pack()
    Button(screen3,text="View Note",command=view_note).pack()
    Label(screen3,text="").pack()
    Button(screen3,text="Delete Note",command=delete_note).pack()
    
    
def login_verify():
    username1=username_reg.get()
    password1=password_reg.get()
    
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)
    
    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines() 
        if password1 in verify:
            notes()
        else:
            Label(screen2,text="Password is incorrect", fg="red").pack()
    else:
        Label(screen2,text="User doesnt exist", fg="red").pack()
    
    

def register_user():
    username_info=username.get()
    password_info=password.get()
    
    if len(username.get())!=0:
        if len(password.get())!=0 and len(rpassword.get())!=0:
            if password.get()==rpassword.get():
                file=open(username_info,"w")
                file.write(username_info+"\n")
                file.write(password_info)
                file.close()
                username_entry.delete(0,END)
                password_entry.delete(0,END)
                rpassword_entry.delete(0,END)
                Label(screen1,text="Registration Successful" ,fg="green").pack()
            else:
                Label(screen1,text="Passwords dont match", fg="red").pack()
        else:
            Label(screen1,text="Password field is empty", fg="Blue").pack()
    else:
        Label(screen1,text="Username field is empty", fg="Blue").pack()

    
    

def sign_up():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Registration")
    screen1.geometry("300x300")
    
    global username
    global password
    global rpassword
    global username_entry
    global password_entry
    global rpassword_entry
    
    username=StringVar()
    password=StringVar()
    rpassword=StringVar()
    
    Label(screen1,text="Please enter the following details",bg="grey",font=("Calibri",13,"bold"),width="300").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username*").pack()
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password*").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text="Re-Enter Password*").pack()
    rpassword_entry=Entry(screen1,textvariable=rpassword)
    rpassword_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Sign Up",font=15,width="10",height="1",bg="grey",command=register_user).pack()

def login_screen():
    global username_reg
    global password_reg
    global screen2
    global username_entry1
    global password_entry1
    
    
    screen2=Toplevel(screen)
    screen2.title("Sign In")
    screen2.geometry("400x400")
    
    
    username_reg=StringVar()
    password_reg=StringVar()
    
    Label(screen2,text="Enter your details",bg="grey",width="300").pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Username").pack()
    username_entry1=Entry(screen2,textvariable=username_reg)
    username_entry1.pack()
    Label(screen2,text="Password").pack()
    password_entry1=Entry(screen2,textvariable=password_reg)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Sign In",font=11,width="10",height="1",bg="grey",command=login_verify).pack()
       
    

def main_screen():
    
    global screen
    screen=Tk()
    screen.geometry("300x300")
    screen.title("Notes")
    Label(text="Notes", font=("Calibri",17,"bold"),width="300",height="2",bg="grey").pack()
    Label(text='').pack()
    Label(text='').pack()
    Button(text="Login",font=15,width="30",height="2",bg="grey",command=login_screen).pack()
    Label(text="").pack()
    Button(text="Sign Up",font=15,width="30",height="2",bg="grey",command=sign_up).pack()
    screen.mainloop()


main_screen()