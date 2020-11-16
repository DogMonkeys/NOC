import random

class Rand:
	@classmethod
	def ch_names(cls):
		names = ['易腐垃圾', '其他垃圾', '有害垃圾', '可回收物']
		k = names[random.randint(0, 4)]
		return k

	@classmethod
	def ch_datas_1(cls, type_, dat):
		sl = dat.RUBBISHS[type_]
		return random.chioce(sl)
