import tkinter

def file_reader():
    global label
    label.destroy()
    with open(input1.get(), 'r') as file:
        content = file.readlines()
        result = ""
        line_num = 1
        for line in content:
            result += (f"Line {line_num}: {line}")
            line_num +=1
    label = tkinter.Label(root, text= result, anchor='w')
    label.grid(row=2, column=1, sticky='w')

root = tkinter.Tk(className="file reader")

label = tkinter.Label(root, text = "")
input1 = tkinter.Entry(root)
input1.grid(row=1, column=1)

submit = tkinter.Button(root, text="Find file", command=file_reader)
submit.grid(row=1, column=2)

if __name__ == '__main__':
    root.mainloop() # creates window and event loop 