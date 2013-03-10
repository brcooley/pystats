from math import sqrt

def mean(data):
	return sum(data) / len(data)


def median(data):
	d = sorted(data)
	half = len(d) // 2
	return float(d[half]) if len(d) % 2 != 0 else (d[half] + d[half + 1]) / 2


def std_dev(data):
	return sqrt(variance(data))


def variance(data):
	return sum((d - mean(data))**2 for d in data) / len(data)