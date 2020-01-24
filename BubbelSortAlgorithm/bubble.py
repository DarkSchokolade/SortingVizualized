# Bubble Sort algorithm
import csv
import time

x=[]
field_names = ["x_value", "y_value"]


with open('BS.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
	csv_writer.writeheader()


def bubblesort(MyList):
	#time.sleep(3)
	for k in range(1, len(MyList)+1):
		x.append(k)
		 
	for i in range(0, len(MyList)-1):
		for j in range(0, len(MyList)-1-i):
			if MyList[j] > MyList[j+1]:
				MyList[j], MyList[j+1] = MyList[j+1], MyList[j]

				with open('BS.csv', 'w') as csv_file:
					csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
					csv_writer.writeheader()

					writer = csv.writer(csv_file)
					writer.writerows(zip(x, MyList))
					print(x,MyList)
				time.sleep(1.1)
	return MyList


list1 = [3, 4, 2, 9, 1, 5, 7, 11, 3, 8, 6]

print(bubblesort(list1))
