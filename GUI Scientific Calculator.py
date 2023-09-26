# Import different packages
from tkinter import *  # Importing all the functions and built-in modules in the tkinter library.
import tkinter  # Importing tkinter module.
import tkinter.messagebox  # The tkinter.messagebox module is used to display the message boxes in the python applications.
import math  # Importing math module to access built-in mathematics functions.
import datetime as dt  # Importing date module (The datetime module supplies classes for manipulating dates and times).
from time import strftime  # Importing strftime() funtion.

'''WINDOW CONFIGURATION'''

tk_calc = Tk()  # Creating root window as tl_calc.
tk_calc.configure(bg="cyan", bd=5)
tk_calc.title("GUI Scientific Calculator")  # Title of GUI window.
# tk_calc.iconbitmap(False,r"C:\Users\7\Downloads\calc.ico") # Setting logo to GUI window.
tk_calc.geometry("280x265")  # Defining size of GUI window.
tk_calc.resizable(0, 0)  # Declaring resizing properties of GUI window.

calc_operator = ""  # Declaring variable as string.
operator = ""  # Declaring operator as string.
text_input = StringVar()  # Holds a string; the default value is an empty string "".

'''MENU-BAR'''


# Defining Exit window confirmation dialogue box.
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
    if iExit > 0:
        tk_calc.destroy()
        return


# Defining key to expanding window to display scientific calculator.
def Scientific():
    tk_calc.resizable(width=False, height=False)
    tk_calc.geometry("280x512")


# Defining key to collapsing window to display only standard calculator.
def Standard():
    tk_calc.resizable(width=False, height=False)
    tk_calc.geometry("280x265")


# Defining date and time keys.
def time():
    string = strftime("%H : %M : %S %p")
    label.config(text=string)
    label.after(1000, time)
    return string


# ManuBar:
menubar = Menu(tk_calc)  # Creating menubar in tk_calc GUI window.
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Menu', menu=filemenu)  # Menu key.
filemenu.add_command(label="Standard", command=Standard)  # Standard calc key inside Menu
filemenu.add_command(label='Scientific', command=Scientific)  # Scientific calc key inside Menu.
menubar.add_cascade(label="Exit", command=iExit)  # Exit key.

''' FUNCTIONS '''


# Function to add in the entry of text display.
def button_click(char):
    global calc_operator
    calc_operator = calc_operator + str(char)
    text_input.set(calc_operator)


# Function to implement division operator in the entry of text display
def button_div():
    global calc_operator
    calc_operator = calc_operator + "/"
    text_input.set(calc_operator)


# Function to clear the whole entry of text display
def button_clear_all():
    global calc_operator
    calc_operator = ""
    text_input.set("")


# Function to delete one by one from the last in the entry of text display
def button_delete():
    global calc_operator
    text = calc_operator[:-1]
    calc_operator = text
    text_input.set(text)


# Function to calculate trigonometric numbers of an angle
def trig_sin():
    global calc_operator
    result = str(round(math.sin(math.radians(float(calc_operator))), 8))
    calc_operator = result
    text_input.set(result)


def trig_cos():
    global calc_operator
    result = str(round(math.cos(math.radians(float(calc_operator))), 8))
    calc_operator = result
    text_input.set(result)


def trig_tan():
    global calc_operator
    result = str(round(math.tan(math.radians(float(calc_operator))), 10))
    calc_operator = result
    text_input.set(result)


# Function to calculate the inverse of trig func.
def trig_asin():
    try:
        global calc_operator
        result = str(round(math.degrees(math.asin(float(calc_operator)))))
        calc_operator = result
        text_input.set(result)
    except Exception:
        tkinter.messagebox.showerror("Domain Error", "Enter value between (-1) to (1).")


def trig_acos():
    try:
        global calc_operator
        result = str(round(math.degrees(math.acos(float(calc_operator)))))
        calc_operator = result
        text_input.set(result)
    except Exception:
        tkinter.messagebox.showerror("Domain Error", "Enter value between (-1) to (1).")


def trig_atan():
    global calc_operator
    result = str(round(math.degrees(math.atan(float(calc_operator))), 8))
    calc_operator = result
    text_input.set(result)


# Function to calculate the factorial of a number
def fact_func():
    try:
        global calc_operator
        result = str(math.factorial(int(calc_operator)))
        calc_operator = result
        text_input.set(result)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Enter an integer")


# Function to calculate the gamma of a number
def gamma_func():
    try:
        global calc_operator
        result = str(round(math.gamma(float(calc_operator)), 10))
        calc_operator = result
        text_input.set(result)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Enter the proper value!")


# Function to find the square root of a number
def square_root():
    try:
        global calc_operator
        temp = str(math.sqrt(float(calc_operator)))
        calc_operator = temp
        text_input.set(temp)
    except Exception:
        tkinter.messagebox.showerror("Value Error", "Enter a positive value")


# Function to change the sign of number
def sign_change():
    global calc_operator
    if calc_operator[0] == '-':
        temp = calc_operator[1:]
    else:
        temp = '-' + calc_operator
    calc_operator = temp
    text_input.set(temp)


# Funtion to find the result of an operation
def button_equal():
    try:
        global calc_operator
        temp_op = str(eval(calc_operator))
        text_input.set(temp_op[:11])
        calc_operator = temp_op
    except ZeroDivisionError as z:
        tkinter.messagebox.showerror("Error", z)
    except SyntaxError as s:
        tkinter.messagebox.showerror("Error", s)
    except ValueError as v:
        tkinter.messagebox.showerror("Error", v)


# Function to calculate the percentage of a number
def percent():
    global calc_operator
    temp = str(eval(calc_operator + '/100'))
    calc_operator = temp
    text_input.set(temp)


# Function to find the third root of a number
def third_root():
    global calc_operator
    if int(calc_operator) >= 0:
        temp = str(eval(calc_operator + '**(1/3)'))
        calc_operator = temp
    else:
        temp = "ERROR"
    text_input.set(temp)


''' Variables '''

sin, cos, tan = math.sin, math.cos, math.tan
log, ln = math.log10, math.log
Γ = math.gamma
e = math.exp
p = math.pi
E = '*10**'

''' VARIABLE FOR FONT STYLISH '''

button_params = {'bd':5,
                 'fg':'black',
                 'bg':'white',
                 'relief':'groove',
                 'font':('Times New Roman', 12)
                 }

button_params_main = {'bd':5,
                      'bg':'white',
                      'fg':'black',
                      'relief':'groove',
                      'font':('Times New Roman', 12)
                      }
font_style_clear_text = {'bd':5,
                         'bg':'orange',
                         'fg':'black',
                         'relief':'groove',
                         'font':('Times New Roman', 9, 'bold')
                         }
font_style_multiplication = {'bd':5,
                             'fg':'black',
                             'bg':'white',
                             'relief':'groove',
                             'font':('Times New Roman', 10)
                             }
font_style_division = {'bd':5,
                       'fg':'black',
                       'bg':'white',
                       'relief':'groove',
                       'font':('Times New Roman', 12, 'bold')
                       }
font_style_equal = {'bd':5,
                    'bg':'orange',
                    'fg':'black',
                    'relief':'groove',
                    'font':('Times New Roman', 10, 'bold')
                    }
exp_font = {'bd':5,
            'bg':'white',
            'fg':'black',
            'relief':'groove',
            'font':('Times New Roman', 10)
            }
font_style_dot = {'bd':5,
                  'bg':'white',
                  'fg':'black',
                  'relief':'groove',
                  'font':('Times New Roman', 10 , 'bold')
                  }
font_style_percentage = {'bd':5,
                         'fg':'black',
                         'bg':'white',
                         'relief':'groove',
                         'font':('Times New Roman', 10)
                         }

''' DATE & TIME '''

F0 = Frame(tk_calc, bg="white")
F0.pack(expand=TRUE, fill=BOTH)
date = dt.datetime.now()
label = Label(F0, text=f"{date:%b %d, %Y (%a)}", font=("Arial", 8, "bold"), fg="black", bg='white')
label.pack(side=LEFT)
label = Label(F0,
              font=("Arial", 8, 'bold'),
              fg="black",
              bg='white')
label.pack(side=RIGHT)
time()

''' TEXT DISPLAY '''

# --Frame 1--
F1 = Frame(tk_calc, bg="black")
F1.pack(expand=TRUE, fill=BOTH)
text_display = Entry(F1, font=('Times New Roman', 22, 'bold'), textvariable=text_input, bd=5, insertwidth=5, relief='groove', bg='#ABCDEF', justify='right')
text_display.pack(side=LEFT, expand=TRUE, fill=BOTH)

''' CALCULATOR MODE (STANDARD) '''

bdr_stndrd = Button(tk_calc, text='Standard', font=('Times New Roman', 12), bg='cyan', relief='groove', justify='right')
bdr_stndrd.pack(expand=TRUE, fill=BOTH)

''' BUTTONS FOR STANDARDS CALCULATOR '''

# --Frame 2--
F2 = Frame(tk_calc, bg="#000000")
F2.pack(expand=TRUE, fill=BOTH)
button_7 = Button(F2, button_params_main, text='7', command=lambda:button_click('7'))
button_7.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=4)
button_8 = Button(F2, button_params_main, text='8', command=lambda:button_click('8'))
button_8.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=4)
button_9 = Button(F2, button_params_main, text='9', command=lambda:button_click('9'))
button_9.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=4)
button_delete_one = Button(F2, font_style_clear_text, text='\u232B', command=button_delete)
button_delete_one.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=2)
button_clear_all = Button(F2, font_style_clear_text, text='AC', command=button_clear_all)
button_clear_all.pack(side=LEFT, expand=TRUE, fill=BOTH)
# --Frame 3--
F3 = Frame(tk_calc, bg="#000000")
F3.pack(expand=TRUE, fill=BOTH)
button_4 = Button(F3, button_params_main, text='4', command=lambda:button_click('4'))
button_4.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=2)
button_5 = Button(F3, button_params_main, text='5', command=lambda:button_click('5'))
button_5.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=1)
button_6 = Button(F3, button_params_main, text='6', command=lambda:button_click('6'))
button_6.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=1)
button_mul = Button(F3, font_style_multiplication, text='X', command=lambda:button_click('*'))
button_mul.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=3)
button_division = Button(F3, font_style_division, text='\xF7', command=lambda:button_click("/"))
# or command =  button_div can be used.
button_division.pack(side=LEFT, expand=TRUE, fill=BOTH)
# --Frame 4--
F4 = Frame(tk_calc, bg="#000000")
F4.pack(expand=TRUE, fill=BOTH)
button_1 = Button(F4, button_params_main, text='1', command=lambda:button_click('1'))
button_1.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_2 = Button(F4, button_params_main, text='2', command=lambda:button_click('2'))
button_2.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_3 = Button(F4, button_params_main, text='3', command=lambda:button_click('3'))
button_3.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_add = Button(F4, button_params_main, text='+', command=lambda:button_click('+'))
button_add.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_sub = Button(F4, button_params_main, text='-', command=lambda:button_click('-'))
button_sub.pack(side=LEFT, expand=TRUE, fill=BOTH)
# --Frame 5--
F5 = Frame(tk_calc, bg="#000000")
F5.pack(expand=TRUE, fill=BOTH)
button_0 = Button(F5, button_params_main, text='0', command=lambda:button_click('0'))
button_0.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=4)
button_dot = Button(F5, font_style_dot, text='.', command=lambda:button_click('.'))
button_dot.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=9)
button_exp = Button(F5, exp_font, text='x10\u02E3', command=lambda:button_click(E))
button_exp.pack(side=LEFT, expand=TRUE, fill=BOTH)
button_equal = Button(F5, font_style_equal, text='=', command=button_equal)
button_equal.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=33)

''' CALCULATOR MODE (SCIENTIFIC) '''

bdr_sci = Button(tk_calc, text='Scientific', font=('Times New Roman', 12), bg='cyan', relief='groove', justify='right')
bdr_sci.pack(expand=TRUE, fill=BOTH)

''' BUTTONS FOR STANDARDS CALCULATOR '''

# --Frame 6--
F6 = Frame(tk_calc, bg="#000000")
F6.pack(expand=TRUE, fill=BOTH)
# Sine of an angle in degrees
sine = Button(F6, button_params, text='sin', command=trig_sin)
sine.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Cosine of an angle in degrees
cosine = Button(F6, button_params, text='cos', command=trig_cos)
cosine.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Tangent of an angle in degrees
tangent = Button(F6, button_params, text='tan', command=trig_tan)
tangent.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Logarithm of a number with base 10
log10 = Button(F6, button_params, text='log', command=lambda:button_click('log('))
log10.pack(side=LEFT, expand=TRUE, fill=BOTH)
# --Frame 7--
F7 = Frame(tk_calc, bg="#000000")
F7.pack(expand=TRUE, fill=BOTH)
# arcsin
asine = Button(F7, button_params, text='sin\u207B\u00B9', command=trig_asin)
asine.pack(side=LEFT, expand=TRUE, fill=BOTH)
# arccos
acos = Button(F7, button_params, text='cos\u207B\u00B9', command=trig_acos)
acos.pack(side=LEFT, expand=TRUE, fill=BOTH)
# arctan
atangent = Button(F7, button_params, text='tan\u207B\u00B9', command=trig_atan)
atangent.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Natural log
loge = Button(F7, button_params, text='ln', command=lambda:button_click('ln('))
loge.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=11)
# --Frame 8--
F8 = Frame(tk_calc, bg="#000000")
F8.pack(expand=TRUE, fill=BOTH)
# Factorial of a number
btnfact = Button(F8, button_params, text='x!', command=fact_func)
btnfact.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Gamma of a number
btngamma = Button(F8, button_params, text='\u0393x', command=lambda:button_click('Γ('))  # gamma_func
btngamma.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Euler's number e
btne = Button(F8, button_params, text='e', command=lambda:button_click(str(math.exp(1))[:11]))
btne.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=4)
# Pi(3.14...) number
btnpi = Button(F8, button_params, text='π', command=lambda:button_click(str(math.pi)[:11]))
btnpi.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=3)
# --Frame 9--
F9 = Frame(tk_calc, bg="#000000")
F9.pack(expand=TRUE, fill=BOTH)
# Square root of a number
square_root = Button(F9, button_params, text='\u221A', command=square_root)
square_root.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=5)
# Power of 2
second_power = Button(F9, button_params, text='x\u00B2', command=lambda:button_click('**2'))
second_power.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=6)
# Power of n
nth_power = Button(F9, button_params, text='x^n', command=lambda:button_click('**'))
nth_power.pack(side=LEFT, expand=TRUE, fill=BOTH)
# Calculate the function e^x
exp = Button(F9, button_params, text='e^x', command=lambda:button_click('e('))
exp.pack(side=LEFT, expand=TRUE, fill=BOTH)
# --Frame 10--
F10 = Frame(tk_calc, bg="#000000")
F10.pack(expand=TRUE, fill=BOTH)
# Add a left parentheses
left_par = Button(F10, button_params, text='(', command=lambda:button_click('('))
left_par.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=2)
# Add a right parentheses
right_par = Button(F10, button_params, text=')', command=lambda:button_click(')'))
right_par.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=4)
# Change the sign of a number
signs = Button(F10, button_params, text='\u00B1', command=sign_change)
signs.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=2)
# Transform number to percentage
percentage = Button(F10, font_style_percentage, text='%', command=percent)
percentage.pack(side=LEFT, expand=TRUE, fill=BOTH, ipadx=2)

''' NOTE '''

note = Button(tk_calc, text='Note: Take angles in degrees', relief='groove', font=('Times New Roman', 10, 'italic'))
note.pack(side=LEFT, fill=BOTH, ipadx=50)

tk_calc.config(menu=menubar)
tk_calc.mainloop()
