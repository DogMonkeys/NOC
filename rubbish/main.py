from .classify.rbscly import Classify
from .check.chmain import Check
import tkinter as tk

class Rmain:
	def __init__(self, root, dat):
		self.root = root
		self.dat = dat
		self.root.title('垃圾分类小工具')
		self.root.geometry('300x100')
		self.root.resizable(0, 0)
		tk.Button(self.root, text='垃 圾 分 类 查 询', command=lambda:Classify(tk.Toplevel(self.root), self.dat).main()).pack()
		tk.Button(self.root, text='垃 圾 分 类 竞 赛', command=lambda:Check(tk.Toplevel(self.root), self.dat).main()).pack()
		tk.Button(self.root, text='  退  出  ', command=self.root.destroy).pack()

	def main(self):
		self.root.mainloop()

def rmain(*args):
	Rmain(*args).main()