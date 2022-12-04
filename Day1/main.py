import sys
sys.path.append("../")
from Models.FileReader import FileReader
from Models.Elf import Elf
import numpy as np

def main():
    # PART 1 OF DAY 1
    file_reader = FileReader("input.txt", "")
    file_reader.read_file()

    calories_per_elf = file_reader.content.split("\n\n")
    calories_mat_str = [substring.split("\n") for substring in calories_per_elf]
    arr_str_counter = 1

    # Contains sum of all food calories per Elf
    arr_sum_calories = []

    elfs_array: Elf = []

    for arr_str in calories_mat_str:
        arr_int = [int(number) for number in arr_str if len(number) > 0]

        elfs_array.append(Elf(f"elf{arr_str_counter}", arr_int))
        arr_str_counter += 1


    for idx in range(len(elfs_array)):
        total_calories = elfs_array[idx].calculate_total_calories()
        arr_sum_calories.append(total_calories)
    
    # SORT HIGHER TO MINOR
    arr_sum_calories.sort(reverse=True)
    
    higher = arr_sum_calories[0]

    print(f"most calories: {higher}")

    # PART 2 OF DAY 1
    three_higher = arr_sum_calories[0:3]
    print(f"Sum of three higher calories= {sum(three_higher)}")

if __name__ == "__main__":
    main()