from input_from_file import input_from_file
from swap_in_list import swap_in_list
from print_in_list import print_in_list

def bubble_sort (array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                swap_in_list(array, i, j)

if __name__ == "__main__":
    input = input_from_file()
    print_in_list("Input", input)

    bubble_sort(input)
    print_in_list("Result", input)
