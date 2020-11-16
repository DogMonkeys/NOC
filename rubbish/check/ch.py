import random

class Rand:
	@classmethod
	def chone(cls, dat):
		names = ['易腐垃圾', '其他垃圾', '有害垃圾', '可回收物']
		k = names[random.randint(0, 4)]
		s = random.choice(dat[k])
		return [k, s]

