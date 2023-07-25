import tkinter

def strip_vowels():
    global label
    label.destroy()
    sentance = input1.get()
    label = tkinter.Label(root, text= ''.join(char for char in sentance if char not in 'aeiouAEIOU'))
    label.grid(row=2, column=1)

root = tkinter.Tk(className="Vowel remover")

label = tkinter.Label(root, text = "")
input1 = tkinter.Entry(root)
input1.grid(row=1, column=1)

submit = tkinter.Button(root, text="strip vowels", command=strip_vowels)
submit.grid(row=1, column=2)
#label.pack() # places object wherever it can on display
#label.grid(row=1, column=1) # allows you to denote a grid corordinate for the label

if __name__ == '__main__':
    root.mainloop() # creates window and event loop 