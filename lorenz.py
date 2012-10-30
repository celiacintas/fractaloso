from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy import arange


def lorenzInt(xyz, t):
	sigma = 10
	rho = 28
	beta = 8.0/3
	return [ sigma * (xyz[1] - xyz[0]),xyz[0] * (rho -xyz[2]) - xyz[1], xyz[0] * xyz[1] - beta* xyz[2]]

if __name__ == '__main__':
	xyzInitial = [0, 1, 1.05]
	t = arange(0, 100, 0.01)
	lorenzSolution = odeint(lorenzInt, xyzInitial, t)
	#plot part
	fig = plt.figure()
	ax = Axes3D(fig)
	ax.plot([x[0] for x in lorenzSolution], 
		[y[1] for y in lorenzSolution], 
		[z[2] for z in lorenzSolution])
	plt.show()
