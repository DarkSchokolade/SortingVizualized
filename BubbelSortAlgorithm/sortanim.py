# animation for sorting algorithm using matplotlib
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.style.use('ggplot')
#print(plt.style.available)
#x = [1, 2, 3, 4, 5, 6]
# y = [1, 2, 3, 4, 9]

def anim(i):
	data = pd.read_csv('BS.csv')
	x = data.x_value
	y = data.y_value

	plt.cla() #plot clear axis

	plt.bar(x, y,color='#960b92', label='BubbelSort Algorithm')
	plt.legend(loc='upper left')
	plt.tight_layout()


ani = FuncAnimation(plt.gcf(), anim, interval=1100)

plt.tight_layout()
plt.show()
