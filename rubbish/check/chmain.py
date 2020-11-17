import tkinter as tk
from .ch import *
from tkinter import messagebox as mb

class Check:
	def __init__(self, root, dat):
		self.crt_asw = None
		self.root = root
		self.dat = dat.RUBBISHS
		self.root.title('垃圾分类知识检测')
		self.root.geometry('300x300')
		self.root.resizable(0, 0)
		self.intv = tk.IntVar()
		self.viewl = tk.Label(self.root, text='等待开始...')
		self.viewl.pack()
		self.rs = [tk.Radiobutton(self.root, text='等待开始...', variable=self.intv, value=i) for i in range(4)]
		tk.Button(self.root, text='开始/重新加载', command=self.flush).pack()#.place(x=100, y=30)
		for k in self.rs:
			k.pack()
		tk.Label(self.root, text='').pack()
		tk.Button(self.root, text='   提  交   ', command=self.check).pack()
		tk.Label(self.root, text='').pack()
		tk.Button(self.root, text='   关  闭   ', command=self.root.destroy).pack()
		self.fs_l = tk.Label(self.root, text='')
		self.fs_l.pack()
		self.count = 0
		self.count_crt = 0
		self.fs_l.config(text='%d / %d   %d %%' % (self.count_crt, self.count, 0))

	def flush(self):
		flag = random.randint(0, 1)
		if flag:
			moban = '%s属于什么垃圾?'
			name = Rand.ch_names()
			print(name)
			x = random.choice(self.dat[name])
			self.viewl.config(text=moban % x)
			ks = list(self.dat.keys())
			ks2 = ks.copy()
			x2 = random.sample(random.sample(ks2.pop(ks2.index(name)), 3) + [name], 4)
			print(ks)
			self.crt_asw, self.nowdt = ks.index(name), [ks, [x]]
			print(self.crt_asw)
			for i, k in enumerate(self.rs):
				k.config(text=ks[i])
		else:
			moban = '下列属于%s的是?'
			name = Rand.ch_names()
			#print(name)
			self.viewl.config(text=moban % name)
			self.nowdt = Rand.ch_datas_4(name, self.dat)
			print(self.nowdt)
			for i, k in enumerate(self.rs):
				k.config(text=self.nowdt[0][i])
			self.crt_asw = self.nowdt[0].index(self.nowdt[1][0])
			print(self.crt_asw)

	def check(self):
		asw = self.intv.get()
		print(asw)
		if asw == self.crt_asw:
			mb.showinfo(title='√', message='答对了!')
			self.count_crt += 1
		else:
			mb.showinfo(title='x', message='答错了..正确答案是：\n%s' % self.nowdt[0][self.crt_asw])
		self.count += 1
		self.flush()
		self.fl()

	def fl(self):
		self.fs_l.config(text='%d / %d   %d %%' % (self.count_crt, self.count, int(100 * (self.count_crt / self.count))))

	def main(self):
		self.root.mainloop()

