import tkinter as tk
from tkinter import messagebox as mb
from json import loads, load, dumps
from tkinter import ttk
from os import popen, mkdir
import os

class Tools:
	names = ['五谷类', '蔬菜类', '水果类', '肉类', '蛋类', '水产类', '奶类', '饮料类', '菌藻类', '油脂']
	@classmethod
	def err(cls, exp=None):
		if exp is None:
			mb.showerror(title='错误', message='没有相关信息')
		else:
			mb.showerror(title='错误', message=exp)

	@classmethod
	def info(cls, title, msg):
		mb.showinfo(title=title, message=msg)

class Food2kll:
	def __init__(self, root, data):
		self.ffoods = []
		self.root = root
		self.root.title('食物的热量')
		self.root.geometry('400x400')
		self.root.resizable(0, 0)
		self.food_dat = data.FOODS
		#print(type(self.food_dat))
		self.maincmb = ttk.Combobox(self.root)
		self.maincmb['value'] = tuple(Tools.names)
		self.maincmb.place(x=60, y=15)
		tk.Label(self.root, text='食物').place(x=30, y=60)
		tk.Label(self.root, text='吃了').place(x=240, y=60)
		tk.Label(self.root, text='*100g').place(x=350, y=60)
		self.soncmb = ttk.Combobox(self.root)
		self.soncmb.place(x=70, y=60)
		self.num_100 = tk.Entry(self.root, width=10)
		self.num_100.place(x=270, y=60)
		self.view_t = tk.Text(self.root)
		self.view_t.place(x=0, y=300)
		tk.Button(self.root, text='更改', command=self.change).place(x=280, y=10)
		tk.Button(self.root, text='     加   入     ', command=self.join).place(x=150, y=110)
		tk.Button(self.root, text='     计   算     ', command=self.run).place(x=150, y=160)
		tk.Button(self.root, text='     保   存     ', command=lambda:self.save(1)).place(x=150, y=210)
		tk.Button(self.root, text='     加   载     ', command=self.loadd).place(x=150, y=260)

	def main(self):
		self.root.mainloop()

	def change(self):
		p = self.maincmb.current()
		print(p)
		if p < 0:
			Tools.err('项目不存在')
			return
		else:
			self.view_t.insert(0.0, '成功将状态更改为：%s\n' % Tools.names[p])
			self.soncmb['value'] = tuple(i[0] for i in self.food_dat[Tools.names[p]])

	def join(self):
		p = self.soncmb.current()
		p_ = self.maincmb.current()
		print(p)
		if p < 0 or p_ < 0:
			Tools.err('项目不存在')
			return
		try:
			self.ffoods.append([self.food_dat[Tools.names[p_]][p], float(self.num_100.get()), float(self.num_100.get())*int(self.food_dat[Tools.names[p_]][p][1])])
		except Exception as e:
			Tools.err(str(e))
		self.flush()

	def flush(self):
		self.view_t.delete(0.0, 'end')
		body = ''
		for k in self.ffoods:
			body += '食物"{}"：{} g 共{}大卡能量;\n'.format(k[0][0], k[1]*100, k[1]*int(k[0][1]))
		self.view_t.insert(0.0, body)

	def run(self):
		bd = 0
		for k in self.ffoods:
			bd += k[2]
		Tools.info('计算结果', str(bd))

	def save(self, flag=0):
		try:
			mkdir('Src\\Foods')
		except:
			for l in os.listdir('Src\\Foods'):
				print(l)
				os.remove('Src\\Foods\\' + l)
		for idx, k in enumerate(self.ffoods):
			cmd = 'Tools\\w_f.exe "%s" "%f" "%d" "%s"' % (repr(k[0]), k[1], k[2], 'Src\\Foods\\save%d.dat' % idx)
			print(cmd)
			with popen(cmd) as f:
				f_ = f.read()
				print(f_)
				if f_ == 'suc':
					pass
				else:
					Tools.err('未知错误')
		if flag:
			Tools.info('保存成功', '保存成功')

	def loadd(self):
		try:
			for k in os.listdir('Src\\Foods'):
				print(k)
				with popen('Tools\\r_f.exe "Src\\Foods\\%s"' % k) as f:
					x = f.read()
					print(x)
					self.ffoods.append(eval(x))
		except Exception as e:
			Tools.err(str(e))
		self.flush()

