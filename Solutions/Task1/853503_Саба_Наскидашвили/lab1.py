import argparse


def txt_input(filename):
    with open(filename, 'r') as f:
        string = f.read()
    text = string.split()
    word = {}.fromkeys(text, 0)
    for a in text:
        word[a] += 1
    print(word)
    w = open("sentence.txt", 'w')
    list_d = sort_dictionary(word)
    counter = 0
    while counter < 10:
        w.write(list_d[counter] + ' ')
        counter += 1
    w.close()


def sort_dictionary(dictionary):
    of_word = [k for k in sorted(dictionary.keys(), key=dictionary.get, reverse=True)]
    return of_word


def merge_sort(number_list):
    if len(number_list) > 1:
        mid = len(number_list) // 2
        left_half = number_list[:mid]
        right_half = number_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                number_list[k] = left_half[i]
                i = i + 1
            else:
                number_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            number_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            number_list[k] = right_half[j]
            j = j + 1
            k = k + 1


def quick_sort(arr, left, right):
    left_side = left
    right_side = right
    pivot = arr[left]
    while left < right:
        while arr[right] >= pivot and left < right:
            right -= 1
        if left != right:
            arr[left] = arr[right]
            left += 1
        while (arr[left] <= pivot) and (left < right):
            left += 1
        if left != right:
            arr[right] = arr[left]
            right -= 1
    arr[left] = pivot
    pivot = left
    left = left_side
    right = right_side
    if left < pivot:
        quick_sort(arr, left, pivot - 1)
    if right > pivot:
        quick_sort(arr, pivot + 1, right)


def fibonacci(n):
    fib1, fib2 = 0,1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of file where there is data", type=str)
parser.add_argument("-w", "--words_in_text", action="store_true")
parser.add_argument("-s", "--sort", action="store_true")
parser.add_argument("-f", "--fibonacci", action="store_true")

args = parser.parse_args()

if args.words_in_text:
    txt_input(args.filename)


elif args.sort:
    with open(args.filename) as from_file:
        txt = from_file.read()
    array = txt.split()
    array = list(map(int, array))
    print(array)
    size = len(array)
    print("Choose the sort:  1.QuickSort  2.MergeSort")
    ch = int(input())
    if ch == 1:
        quick_sort(array, 0, size - 1)
        print(array)
    else:
        merge_sort(array)
        print(array)

elif args.fibonacci:
    with open(args.filename) as fib_number:
        numb = int(fib_number.read())
    result = list(fibonacci(numb))
    print(result)


