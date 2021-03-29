#this is a python program for remotely transmiting data

#first part generate a list with lenght of 60 for 60sec in a min
import tkinter, time
from tkinter import *


def lisgen():
    lis= list()
    for i in range(0,60):
        lis[i]=0
    return lis

def arraycheck():
    while True:
        usrinput = raw_input("press 1 for view curret reading \n
        for check history")

        if int(usrinput) == 1:
            return 1
        if int(usrinput) == 2:
            return 2
        else:
            print("invalid input please try again")

def feed_data():




def main():
    in_array = lisgen()
    usr_selection = arraycheck()
    if usr_selection == 1:
        feed_data()
    if usr_selection == 2:
        return
        #open file location
