import tkinter as tk
from tkinter import messagebox as mb

class Tools:
	@classmethod
	def err(cls, exp=None):
		if exp is None:
			mb.showerror(title='错误', message='没有相关信息')
		else:
			mb.showerror(title='错误', message=exp)

	@classmethod
	def info(cls, title, msg):
		mb.showinfo(title=title, message=msg)

class Classify:
	def __init__(self, root, datt):
		self.root = root
		self.RUBBISHS = datt.RUBBISHS
		self.root.title('垃圾分类查询')
		self.root.geometry('120x70')
		self.root.resizable(0, 0)
		self.ent_w = tk.Entry(self.root, width=10)
		self.ent_w.place(x=20, y=0)
		tk.Button(self.root, text='查询', command=self.find).place(x=40, y=30)

	def find(self):
		key = self.ent_w.get()
		b = []
		if not key:
			Tools.err('关键字为空')
			return
		for i in self.RUBBISHS:
			for k in self.RUBBISHS[i]:
				for key_ in key:
					if key_ in k and key_ != '子' and not [i, k] in b and key_ != '旧':
						b.append([i, k])
		bdy = '查询结果\n'
		for k in b:
			bdy += '%s : 它属于%s\n' % (k[1], k[0])
		Tools.info('查询结果', bdy)

	def main(self):
		self.root.mainloop()
