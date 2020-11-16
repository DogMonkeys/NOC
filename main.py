import tkinter as tk
import os
from tkinter import messagebox as mb
from kll_sum.kll_main import main as run
from Data import data

main_bg = None
class NOC(object):
	def __init__(self, **kw):
		self.root = tk.Tk()
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
		tk.Button(self.root, text='二氧化碳排放模型', command=self.cmd2).place(x=105, y=10)
		# self.ent_path = tk.Entry(self.root, width=35)
		# self.ent_path.insert(0, '工作目录(项目储存位置)')
		# self.ent_path.place(x=20, y=150)
		# tk.Button(self.root, text='  提交  ', command=self.ch).place(x=200, y=170)

	def main(self):
		self.root.mainloop()

	def ch(self):
		pth = self.ent_path.get()
		try:
			os.chdir(pth)
		except:
			mb.showerror(title='路径错误', message='无效的路径:%s' % pth)
		self.ent_path.delete(0, 'end')
		self.ent_path.insert(0, os.getcwd())


def main():
	noc = NOC(c1=lambda:run(data), c2=lambda :print("cc2"))
	noc.main()

if __name__ == '__main__':
	main()