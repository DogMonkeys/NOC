import tkinter as tk
import os
from tkinter import messagebox as mb
from kll_sum.kll_main import main as run
from Data import data
from rubbish.main import rmain

main_bg = None
class NOC(object):
	def __init__(self, **kw):
		self.root = kw['root']
		self.cmd1, self.cmd2 = kw['c1'], kw['c2']
		self.root.title('健康生活小工具')
		self.root.geometry('300x200')
		self.root.resizable(0, 0)
		self.init()

	def init(self):
		global main_bg
		main_bg = tk.PhotoImage(file='Data\\bg.gif')
		tk.Label(self.root, image=main_bg).pack()
		tk.Button(self.root, text='卡路里计算器', command=self.cmd1).place(x=105, y=90)
		tk.Button(self.root, text='垃圾分类', command=self.cmd2).place(x=105, y=10)

	def main(self):
		self.root.mainloop()

def main():
	r = tk.Tk()
	noc = NOC(root=r, c1=lambda:run(data, tk.Toplevel(r)), c2=lambda:rmain(tk.Toplevel(r), data))
	noc.main()

if __name__ == '__main__':
	main()