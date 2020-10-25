#Busqueda binaria -> busca un elemento dentro de una lista ordenada y devuelve su posicion dentro de ella en O(log n)



def binary_search(list, item):
	low = 0
	high = len(list) - 1

	while low <= high:
		mid = (low + high)
		guess = list[mid]
		if guess == item:
			return mid 
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

print(binary_search(my_list, 10))

print(binary_search(my_list, 25))