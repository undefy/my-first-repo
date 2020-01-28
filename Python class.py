# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("hello world")
x=4+5
print (x)
#%%
x=str('hello')
print (x)

"I'm called \"pepe\", but lol"
#%%

type('2')
#%%
hours = input("Let me conver hours to seconds for you. Input hours: ")

try:
    x = int(hours)
    sec=x*60*60
    #SEC=str(sec)
    print("You have selected " + hours + " this is " + str(sec) + " sec.")
except ValueError:
    print("Use only even numbers")
    
print( 2 + (3 + 4) + (5 * 33 ** 34))

momage = input("what is your mother age?")
age = input("what is your age?")
diff = int(momage) - int(age)
print("Difference in age is " + str(diff))

 print("3 * 5 * 2 is " +str(3 * 5 * 2))
 print(3 / 11)
 print(3 // 11)
 print(25 % 2)
    
 
    
    #%%
    
 3.14*2**2
(4/3)*3.14*2**3

print(int(float("3.2")))

#%%
from datetime import date
year = date.today().year
age = input("Whats your age: ")

born=int(year)-int(age)
print("You were born in " +str(born))

#%%
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Prasant dont press\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Why did you do it?!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
#%%
def area_sqr(side):
    if type(side) == int or type(side) == float:
        return side**2
    else:
        print("value is not int")
    
area_sqr(4)

#%%
1. Create a function ~weekly_commute_time~ that asks the user their
   daily commute time and returns their weekly time spent commuting.

print ("How minutes a day do you travel?")
time = int(input())

def weekly_commute_time(time):
    return time*7
weekly_commute_time(time)

2. What do the following expressions return?
   1. ~True or 11 > 34~
   2. ~False and (1 == 1)~
   3. ~(77 // 11) > 6 and False~
   
77//11

3. Create a function ~area_triangle~ that takes the base and height of
   a triangle and returns its area

4. Create function ~area_triangle_rectangle~ that takes the base,
   height, and the kind of shape and calculates its area.  It should
   work for both triangles and rectangles.

5. Create a function ~im_in_love~ that takes a weekday number (from
   monday to friday), and returns how that weekday is (according to
   The Cure!):

   > I don't care if Monday's blue
   > Tuesday's grey and Wednesday too
   > Thursday I don't care about you
   > It's Friday, I'm in love


#lol



