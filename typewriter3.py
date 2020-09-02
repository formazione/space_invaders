import sys, time
from random import randrange
from tkinter import filedialog


x = sys.stdin.read
def texttime(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        if c != " ":
            # if randrange(1, 3) == 2:
                time.sleep(0.1)


filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = (("py","*.py"),("all files","*.*")))
print(filename)
with open(filename) as file:
    text = file.read()
texttime(text)