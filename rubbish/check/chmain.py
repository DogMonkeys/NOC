import tkinter as tk
from ch import *
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
			self.crt_asw, self.nowdt = ks.index(name), [x2, [x]]
			print(self.crt_asw)
			for i, k in enumerate(self.rs):
				k.config(text=self.nowdt[0][i])
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
		else:
			mb.showinfo(title='x', message='答错了..正确答案是：\n%s' % self.nowdt[0][self.crt_asw])
		self.flush()

	def main(self):
		self.root.mainloop()

class d:
	RUBBISHS = {
		"易腐垃圾": [
		"菜叶",
		"橙皮",
		"葱",
		"饼干",
		"蕃茄酱",
		"蛋壳",
		"西瓜皮",
		"马铃薯",
		"鱼骨",
		"甘蔗",
		"玉米",
		"骨头",
		"虾壳",
		"面包",
		"蛋糕",
		"草莓",
		"西红柿",
		"梨",
		"蟹壳",
		"香蕉皮",
		"辣椒",
		"巧克力",
		"茄子",
		"豌豆皮",
		"苹果",
		"树叶"
		],
		"其他垃圾": [
		"旧浴缸",
		"盆子",
		"坏马桶",
		"旧水槽",
		"贝壳",
		"化妆刷",
		"坛子",
		"海绵",
		"花生壳",
		"菜板",
		"砖块",
		"卫生纸",
		"篮球",
		"桃核",
		"杯子",
		"陶瓷碗",
		"一次性筷子",
		"西梅核",
		"坏的花盆",
		"木质梳子",
		"脏污衣服",
		"烟蒂",
		"渣土",
		"湿垃圾袋",
		"瓦片",
		"扫把"
		],
		"有害垃圾": [
		"漆桶",
		"电池",
		"打火机",
		"创口贴",
		"酒精",
		"调色板",
		"油漆",
		"过期的胶囊药物",
		"过期药片",
		"温度计",
		"荧光灯",
		"蓄电池",
		"医用棉签",
		"杀虫剂",
		"水彩笔",
		"农药瓶",
		"医用纱布",
		"口服液瓶",
		"香水瓶",
		"荧光棒",
		"过期化妆品",
		"发胶",
		"注射器",
		"废弃灯泡",
		"煤气罐",
		"医用手套"
		],
		"可回收物": [
		"塑料瓶",
		"食品罐头",
		"玻璃瓶",
		"易拉罐",
		"报纸",
		"旧书包",
		"旧手提包",
		"旧鞋子",
		"牛奶盒",
		"旧塑料篮子",
		"旧玩偶",
		"玻璃壶",
		"旧铁锅",
		"垃圾桶",
		"旧镜子",
		"牙刷",
		"塑料梳子",
		"旧帽子",
		"旧夹子",
		"废锁头",
		"牙膏皮",
		"雨伞骨架",
		"旧纸袋",
		"纸盒",
		"旧玩具"
		]
	}

Check(tk.Tk(), d).main()