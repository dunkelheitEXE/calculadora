from tkinter import *
import parser

window = Tk()
window.title('Claculadora')

# Functions
# Get Numbers function
# - First: We need to safe the index for display
i = 0
def getNumbers(n):
    global i
    display.insert(i, n)
    # Dentro del display los numeros se distribuyen a traves del
    # de la poscicion o mejor conocido como indice
    # El indice lo guardaremos en una variable para que asi
    # cuando escribamos un numero este se añada al final
    # o sea en la poscicion correcta
    i+=1
    
def getOperator(op):
    global i
    lengop = len(op)
    display.insert(i, op)
    i+=lengop

def clearDisplay():
    display.delete(0, END)

def clearOneStep():
    global i
    i -= 1
    display.delete(i, END)

def calculate():
    global i
    state = display.get()
    try:
        math_expression = parser.expr(state).compile()
        result = eval(math_expression)
        clearDisplay()
        display.insert(0, result)
    except expression as identifier:
        clearDisplay()
        display.insert(0, "Error")

# Pantalla de numeros
display = Entry(window)
display.grid(row = 0, columnspan = 6, sticky = W+E)

# Buttons
Button(window, text = "1", command = lambda:getNumbers(1)).grid(row = 3, column = 0, sticky=W+E)
Button(window, text = "2", command = lambda:getNumbers(2)).grid(row = 3, column = 1, sticky=W+E)
Button(window, text = "3", command = lambda:getNumbers(3)).grid(row = 3, column = 2, sticky=W+E)
Button(window, text = "4", command = lambda:getNumbers(4)).grid(row = 2, column = 0, sticky=W+E)
Button(window, text = "5", command = lambda:getNumbers(5)).grid(row = 2, column = 1, sticky=W+E)
Button(window, text = "6", command = lambda:getNumbers(6)).grid(row = 2, column = 2, sticky=W+E)
Button(window, text = "7", command = lambda:getNumbers(7)).grid(row = 1, column = 0, sticky=W+E)
Button(window, text = "8", command = lambda:getNumbers(8)).grid(row = 1, column = 1, sticky=W+E)
Button(window, text = "9", command = lambda:getNumbers(9)).grid(row = 1, column = 2, sticky=W+E)
Button(window, text = "0", command = lambda:getNumbers(0)).grid(row = 4, column = 1, sticky=W+E)

Button(window, text = "=", command = lambda:calculate()).grid(row = 4, column = 0, sticky = W+E)
Button(window, text = "+", command = lambda:getOperator("+")).grid(row = 1, column = 3, sticky = W+E)
Button(window, text = "-", command = lambda:getOperator("-")).grid(row = 2, column = 3, sticky = W+E)
Button(window, text = "*", command = lambda:getOperator("*")).grid(row = 3, column = 3, sticky = W+E)
Button(window, text = "/", command = lambda:getOperator("/")).grid(row = 4, column = 2, sticky = W+E)
Button(window, text = "^2", command = lambda:getOperator("**2")).grid(row = 1, column = 4, sticky = W+E)
Button(window, text = "(", command = lambda:getOperator("(")).grid(row = 2, column = 4, sticky = W+E)
Button(window, text = ")", command = lambda:getOperator(")")).grid(row = 3, column = 4, sticky = W+E)

Button(window, text = "AC", command = lambda:clearDisplay()).grid(row = 4, column = 3, sticky = W+E)
Button(window, text = "<-", command = lambda:clearOneStep()).grid(row = 4, column = 4, sticky = W+E)


window.mainloop()