import random

class Rand:
	@classmethod
	def ch_names(cls):
		names = ['易腐垃圾', '其他垃圾', '有害垃圾', '可回收物']
		k = names[random.randint(0, 3)]
		return k

	@classmethod
	def ch_datas_1(cls, type_, dat):
		sl = dat.RUBBISHS[type_]
		return random.choice(sl)

	@classmethod
	def ch_datas_4(self, type_, dat):
		names = ['易腐垃圾', '其他垃圾', '有害垃圾', '可回收物']
		idx = names.index(type_)
		sl = dat[type_]
		sl2 = dat[names[(idx + random.randint(0, 9)) % 4]]
		x = random.sample(sl, 1)
		print(x)
		return [random.sample(x + random.sample(sl2, 3), 4), x]