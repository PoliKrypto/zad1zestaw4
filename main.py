import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.input = tk.Text(self, height=10, width=20, font=('Arial', 30))
        self.input.pack(side='left')

        self.output = tk.Text(self, height=10, width=20, font=('Arial', 30))
        self.output.pack(side='right')

        self.encypt = tk.Button(self, text='>>>', command=self.encypt)
        self.encypt.pack(side='bottom')

        self.decrypt = tk.Button(self, text='<<<', command=self.decrypt)
        self.decrypt.pack(side='bottom')

    def encypt(self):
        text = self.input.get('1.0', tk.END)

        # TODO implement decrypting function

        self.output.delete('1.0', tk.END)
        self.output.insert(index='1.0height=10, width=20, font=('Arial', 20)', chars=text)

    def decrypt(self):
        text = self.output.get('1.0', tk.END)

  ion

        self.input.delete('1.0', tk.END)
        self.input.insert(index='1.0', chars=text)

root = tk.Tk()
app = Application(master=root)

app.mainloop()