import tkinter as tk
from json import loads, dumps
from tkinter import messagebox
from os import popen

class Sports2kll:
	def __init__(self, root, data):
		self.root = root
		self.data = data
		self.root.title('看看你的运动可以消耗多少能量?')
		self.root.geometry('270x380')
		self.root.resizable(0, 0)
		self.init()

	def init(self):
		tk.Label(self.root, text='跑步(小时):').place(x=10, y=0)
		tk.Label(self.root, text='跳绳(小时):').place(x=10, y=40)
		tk.Label(self.root, text='游泳(小时):').place(x=10, y=80)
		tk.Label(self.root, text='走路(小时):').place(x=10, y=120)
		tk.Button(self.root, text='   清空   ', command=self.dels).place(x=110, y=170)
		tk.Button(self.root, text='   保存   ', command=lambda:self.save(flag=1)).place(x=110, y=210)
		tk.Button(self.root, text='   加载   ', command=self.loadd).place(x=110, y=250)
		tk.Button(self.root, text='   计算   ', command=self.run).place(x=110, y=290)
		tk.Button(self.root, text='   记录   ', command=self.shows).place(x=110, y=330)
		self.run_e = tk.Entry(self.root)
		self.run_e.place(x=90, y=0)
		self.rap_e = tk.Entry(self.root)
		self.rap_e.place(x=90, y=40)
		self.swim_e = tk.Entry(self.root)
		self.swim_e.place(x=90, y=80)
		self.walk_e = tk.Entry(self.root)
		self.walk_e.place(x=90, y=120)
		self.entryl = [self.run_e, self.rap_e, self.swim_e, self.walk_e]

	def dels(self):
		for k in self.entryl:
			k.delete(0, 'end')

	def save(self, flag=0):
		_f = popen(('Tools\\w_s.exe "%s" "%s" "%s" "%s"' % tuple([i.get() for i in self.entryl])) + ' "Src\\Sports\\save.dat"')
		f = True if _f.read() == 'suc' else False
		if f:
			if flag:
				messagebox.showinfo(title='数据保存成功', message='成功！')
		else:
			self.err()
		_f.close()

	def loadd(self):
		try:
			l = loads(self.datt())
			for idx, v in enumerate(self.entryl):
				v.delete(0, 'end')
				v.insert(0, l[idx])
		except Exception as e:
			self.err(str(e))

	def run(self):
		self.save()
		body = 0
		try:
			for i, l in enumerate(self.entryl):
				body += float(l.get()) * self.data.ALL[i]
			messagebox.showinfo(title='计算成功', message='您消耗的卡路里数值为%d' % body)
		except Exception as e:
			self.err(str(e))

	def datt(self):
		_f = popen('Tools\\r_s.exe "Src\\Sports\\save.dat"')
		_f.encoding = 'utf-8'
		x = _f.read()
		print(x)
		_f.close()
		return x

	def main(self):
		self.root.mainloop()

	def err(self, msg=''):
		messagebox.showerror(title='失败', message='不可预知的错误:\n%s' % msg)

	def shows(self):
		try:
			bd = '运动记录如下：\n跑步：{}小时\n跳绳：{}小时\n游泳：{}小时\n走路：{}小时\n'.format(*loads(self.datt()))
			messagebox.showinfo(title='成功！', message=bd)
		except Exception as e:
			self.err(str(e))

