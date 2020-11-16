import tkinter as tk
from ch import *

class Check:
	def __init__(self, root, dat):
		self.root = root
		self.dat = dat
		self.root.title('垃圾分类知识检测')
		self.root.geometry('300x300')
		self.root.resizable(0, 0)
		self.intv = tk.IntVar()
		self.viewl = tk.Label(self.root, text='等待开始...')
		self.viewl.pack()
		self.rs = [tk.Radiobutton(self.root, text='等待开始...', variable=self.intv, value=i) for i in range(4)]
		tk.Button(self.root, text='开始/重新加载').pack()#.place(x=100, y=30)
		for k in self.rs:
			k.pack()
		tk.Label(self.root, text='').pack()
		tk.Button(self.root, text='   提  交   ').pack()
		tk.Label(self.root, text='').pack()
		tk.Button(self.root, text='   关  闭   ', command=self.root.destroy).pack()

	def flush(self):
		pass

	def main(self):
		self.root.mainloop()

Check(tk.Tk(), '').main()