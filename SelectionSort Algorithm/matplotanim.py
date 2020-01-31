# animation for sorting algorithm using matplotlib
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation


plt.style.use('seaborn-pastel')

def anim(i):
	data = pd.read_csv('SelSort.csv')
	x = data.x_value
	y = data.y_value

	plt.cla() #plot clear axis

	plt.bar(x, y,color='g', label='SelectionSort Algorithm')
	plt.legend(loc='upper left')
	plt.tight_layout()


ani = FuncAnimation(plt.gcf(), anim, interval=1100)

plt.tight_layout()
plt.show()
