from abc import ABC, abstractmethod


class Cart():
	def __init__(self, number, speed, length, time):
		self.speed = speed
		self.number = number
		self.length = length
		self.time = time

	def distance_to_finish(self):
		return self.length - self.speed * self.time % self.length


class Car(Cart):
	def __init__(self, number, speed, length, time, type):
		super().__init__(number, speed, length, time)
		if type == 95:
			self.speed = 9 * self.speed // 10
		elif type == 92:
			self.speed = 8 * self.speed // 10

class Motorcycle(Cart):
	def __init__(self, number, speed, length, time, type):
		super().__init__(number, speed, length, time)
		if type == 95:
			self.speed = 8 * self.speed // 10
		elif type == 92:
			self.speed = 6 * self.speed // 10

def main():
	dist_dict = {}
	N, M, t = map(int, input().split())
	for i in range(N):
		vhcl = tuple(map(int, input().split()))
		# print(vhcl)
		if vhcl[1] == 1:
			dist_dict[vhcl[0]] = Car(vhcl[0], vhcl[2], M, t, vhcl[3]).distance_to_finish()
		elif vhcl[1] == 2:
			dist_dict[vhcl[0]] = Motorcycle(vhcl[0], vhcl[2], M, t, vhcl[3]).distance_to_finish()
		elif vhcl[1] == 3:
			dist_dict[vhcl[0]] = Cart(vhcl[0], vhcl[2], M, t).distance_to_finish()
	
	minval = min(dist_dict.values())
	min_numbers = [k for k, v in dist_dict.items() if v == minval]
	print(min(min_numbers))



if __name__ == '__main__':
	main()