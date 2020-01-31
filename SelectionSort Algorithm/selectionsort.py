#selection sort algorithm
import time
import csv

x=[]
field_names = ['x_value', 'y_value']

def selection_sort(A):

	for k in range(1, len(A)+1):
		x.append(k)


	for i in range(0, len(A)-1):
		minIndex = i
		for j in range(i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j

		if i != minIndex:
			time.sleep(1)
			A[i], A[minIndex] = A[minIndex], A[i]

			with open('SelSort.csv', 'w') as csv_file:
				csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
				csv_writer.writeheader()

				writer = csv.writer(csv_file)
				writer.writerows(zip(x, A))
	#return A
			print(A)

list2 = [7, 8, 5, 4, 9, 2, 6, 3, 11, 10, 1]
list1 = [7, 2, 5, 9, 8, 4]
selection_sort(list2)
