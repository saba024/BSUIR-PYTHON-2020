import argparse

def txt_input(filename):
	with open(filename,'r') as f:
		txt = f.read()
	text = txt.split()
	word = {}.fromkeys(text, 0)
	for a in text:
	    word[a] += 1
	print(word)
	w = open("sentence.txt",'w')
	list_d = sort_dictionary(word)
	counter = 0;
	while counter < 10:
	    w.write(list_d[counter] + ' ' )
	    counter += 1
	w.close()

def sort_dictionary(dictionary):
	of_word = [(k) for k in sorted(dictionary.keys(), key = dictionary.get, reverse = True)]
	return of_word
    


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    
def quickSort(arr, left, right):
	left_side = left
	right_side = right
	pivot = arr[left]
	while(left < right):
		while (arr[right] >= pivot and left < right):
			right -= 1
		if(left != right):
			arr[left] = arr[right]
			left += 1
		while((arr[left] <= pivot) and (left < right)):
			left += 1
		if(left != right):
			arr[right] = arr[left]
			right -= 1
	arr[left] = pivot
	pivot = left
	left = left_side
	right = right_side
	if(left < pivot):
		quickSort(arr, left, pivot - 1)	
	if(right > pivot):
		quickSort(arr, pivot + 1, right)


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1



parser = argparse.ArgumentParser()
parser.add_argument("filename",help = "the name of file where there is data", type = str)
parser.add_argument("-w","--words_in_text", action = "store_true")
parser.add_argument("-s","--sort", action = "store_true" )
parser.add_argument("-f","--fibonacci", action = "store_true")

args = parser.parse_args()

if args.words_in_text:
	txt_input(args.filename)


elif args.sort:
	with open(args.filename) as from_file:
		txt = from_file.read()
	array = txt.split()
	array = list(map(int, array))
	print (array)
	size = len(array)
	print("Choose the sort:  1.QuickSort  2.MergeSort")
	ch = int(input())
	if (ch == 1):
		quickSort(array, 0, size - 1)
		print(array)
	else: 
		mergeSort(array)
		print(array)

elif args.fibonacci:
	with open(args.filename) as fib_number:
		numb = int(fib_number.read())
	result = list(fibonacci(numb)) 
	print(result)



