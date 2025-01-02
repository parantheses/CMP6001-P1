import time
import random

def perform_selection_sort(array):
    """
    Selection Sort:
    For each position i, find the smallest element in array[i...end]
    and swap it with the element at position i.
    Complexity: O(n^2).
    """
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

def perform_bubble_sort(array):
    """
    Bubble Sort:
    Repeatedly compare adjacent pairs and swap them if needed.
    After each pass, the largest element bubbles up to the end.
    Complexity: O(n^2).
    """
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def perform_insertion_sort(array):
    """
    Insertion Sort:
    Build a sorted portion by inserting each new element
    into the correct position of the already-sorted part.
    Complexity: O(n^2) in average/worst case.
    """
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1
        # Shift larger elements one position to the right
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_value
    return array

def merge_two_sorted_lists(left, right):
    """
    Merges two sorted lists (left and right) into a single sorted list.
    Used by merge sort.
    """
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    # Append any remaining elements
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    return merged_list

def perform_merge_sort(array):
    """
    Merge Sort:
    Splits the array into halves, sorts each half recursively,
    then merges them back together.
    Complexity: O(n log n).
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = perform_merge_sort(array[:mid])
    right_half = perform_merge_sort(array[mid:])

    return merge_two_sorted_lists(left_half, right_half)

def perform_quick_sort(array):
    """
    Quick Sort:
    Chooses a pivot (here, last element), partitions the array,
    then recursively sorts each side of the pivot.
    Avg. Complexity: O(n log n). Worst: O(n^2).
    """

    def partition(low, high):
        pivot = array[high]
        smaller_index = low - 1
        for current_index in range(low, high):
            if array[current_index] < pivot:
                smaller_index += 1
                array[smaller_index], array[current_index] = (
                    array[current_index],
                    array[smaller_index],
                )
        array[smaller_index + 1], array[high] = array[high], array[smaller_index + 1]
        return smaller_index + 1

    def quicksort_recursive(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quicksort_recursive(low, pivot_index - 1)
            quicksort_recursive(pivot_index + 1, high)

    quicksort_recursive(0, len(array) - 1)
    return array

def main():
    """
    Main function to:
    1) Generate arrays of three sizes.
    2) Apply each sorting algorithm.
    3) Measure and display the time taken for each.
    """
    array_sizes = [10**2, 10**3, 10**4]
    timing_results = {}

    for size in array_sizes:
        # Prepare a random list of integers in [1..1000]
        random_list = [random.randint(1, 1000) for _ in range(size)]

        # 1) Selection Sort
        copy_sel = random_list[:]
        start_sel = time.time()
        perform_selection_sort(copy_sel)
        end_sel = time.time()

        # 2) Bubble Sort
        copy_bub = random_list[:]
        start_bub = time.time()
        perform_bubble_sort(copy_bub)
        end_bub = time.time()

        # 3) Insertion Sort
        copy_ins = random_list[:]
        start_ins = time.time()
        perform_insertion_sort(copy_ins)
        end_ins = time.time()

        # 4) Merge Sort
        copy_mer = random_list[:]
        start_mer = time.time()
        perform_merge_sort(copy_mer)
        end_mer = time.time()

        # 5) Quick Sort
        copy_quick = random_list[:]
        start_quick = time.time()
        perform_quick_sort(copy_quick)
        end_quick = time.time()

        # Record timing in a dictionary
        timing_results[size] = (
            end_sel - start_sel,
            end_bub - start_bub,
            end_ins - start_ins,
            end_mer - start_mer,
            end_quick - start_quick,
        )

    # Display results in a basic table
    print("\n" + "=" * 65)
    print(" Empirical Sorting Times (in seconds) ".center(65))
    print("=" * 65)
    header = f"{'Size':>8} | {'Sel':>9} | {'Bub':>9} | {'Ins':>9} | {'Mer':>9} | {'Quick':>9}"
    print(header)
    print("-" * 65)
    for size in array_sizes:
        sel_t, bub_t, ins_t, mer_t, qui_t = timing_results[size]
        row = f"{size:>8} | {sel_t:>9.5f} | {bub_t:>9.5f} | {ins_t:>9.5f} | {mer_t:>9.5f} | {qui_t:>9.5f}"
        print(row)
    print("=" * 65)

if __name__ == "__main__":
    main()
