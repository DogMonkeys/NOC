import tkinter as tk
from .s2k.sports2kll import Sports2kll as k
from .f2k.foods2kll import Food2kll as f

class KLL:
	def __init__(self, dat, root):
		self.root = root
		self.root.title('卡路里计算器')
		self.root.geometry('300x100')
		self.root.resizable(0, 0)
		tk.Button(self.root, text='   运  动  ->  能  量   ', command=lambda:k(tk.Toplevel(self.root), dat).main).pack()
		tk.Button(self.root, text='   食  物  ->  能  量   ', command=lambda:f(tk.Toplevel(self.root), dat).main).pack()
		tk.Button(self.root, text='   退  出   ', command=self.root.destroy).pack()

	def main(self):
		self.root.mainloop()

def main(datt, root):
	k = KLL(datt, root)
	k.main()

if __name__ == '__main__':
	main()#k(tk.Toplevel(self.root)).main