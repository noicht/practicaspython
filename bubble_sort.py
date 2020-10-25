#Bubble sort o Ordenamiento por burbujeo

def bubbleSort(myList):
	
	for i in range(0, len(myList)-1):
		
		for j in range(0, len(myList)-1-i):
			 	
			if myList[j] > myList[j+1]:
		

				myList[j], myList[j+1] = myList[j+1], myList[j]  
				
				
			  

	return myList
	

listaMartin = [3, 1, 4, 5, 2, 6 ,7]

print(bubbleSort(listaMartin))
