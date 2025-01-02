import time
import random

def perform_selection_sort(array):
    """
    Selection Sort:
    Finds the minimum element in the unsorted part of the array,
    then places it at the beginning. Complexity: O(n^2).
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
    Compares adjacent elements, swapping them if out of order.
    Each pass moves the largest element to the end. Complexity: O(n^2).
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
    Builds a sorted sub-list by inserting each element
    into the correct position. Complexity: O(n^2) average/worst.
    """
    for i in range(1, len(array)):
        current_val = array[i]
        j = i - 1
        while j >= 0 and array[j] > current_val:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_val
    return array

def merge_two_sorted_lists(left, right):
    """
    Merges two sorted lists into a single sorted list.
    Used as a helper in Merge Sort.
    """
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append any leftover elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def perform_merge_sort(array):
    """
    Merge Sort:
    Uses divide-and-conquer. Splits the array, recursively sorts each half,
    then merges. Complexity: O(n log n).
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = perform_merge_sort(array[:mid])
    right = perform_merge_sort(array[mid:])
    return merge_two_sorted_lists(left, right)

def perform_quick_sort(array):
    """
    Quick Sort:
    Selects a pivot (here, last element). Partitions array around pivot,
    then recursively sorts sub-lists. Average O(n log n), worst O(n^2).
    """

    def partition(low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(array) - 1)
    return array

def main():
    # We will run each sorting algorithm multiple times on each array size
    number_of_runs = 5

    array_sizes = [10**2, 10**3, 10**4]
    # We'll store average times in a dictionary keyed by array size
    # Each value will be a dictionary of { "Selection Sort": average_time, ... }
    timing_results = {}

    for size in array_sizes:
        # Generate a random base list for this size
        base_list = [random.randint(1, 1000) for _ in range(size)]

        # For each algorithm, we'll do multiple runs and calculate average
        alg_times = {}

        # 1) Selection Sort
        total_time = 0
        for _ in range(number_of_runs):
            copy_list = base_list[:]
            start = time.time()
            perform_selection_sort(copy_list)
            end = time.time()
            total_time += (end - start)
        alg_times["Selection Sort"] = total_time / number_of_runs

        # 2) Bubble Sort
        total_time = 0
        for _ in range(number_of_runs):
            copy_list = base_list[:]
            start = time.time()
            perform_bubble_sort(copy_list)
            end = time.time()
            total_time += (end - start)
        alg_times["Bubble Sort"] = total_time / number_of_runs

        # 3) Insertion Sort
        total_time = 0
        for _ in range(number_of_runs):
            copy_list = base_list[:]
            start = time.time()
            perform_insertion_sort(copy_list)
            end = time.time()
            total_time += (end - start)
        alg_times["Insertion Sort"] = total_time / number_of_runs

        # 4) Merge Sort
        total_time = 0
        for _ in range(number_of_runs):
            copy_list = base_list[:]
            start = time.time()
            perform_merge_sort(copy_list)
            end = time.time()
            total_time += (end - start)
        alg_times["Merge Sort"] = total_time / number_of_runs

        # 5) Quick Sort
        total_time = 0
        for _ in range(number_of_runs):
            copy_list = base_list[:]
            start = time.time()
            perform_quick_sort(copy_list)
            end = time.time()
            total_time += (end - start)
        alg_times["Quick Sort"] = total_time / number_of_runs

        # Store results for this size
        timing_results[size] = alg_times

    # Print results in a table
    print("\n" + "=" * 80)
    print("Empirical Sorting Times (Averaged Over Multiple Runs)".center(80))
    print("=" * 80)
    # Print header
    print(f"{'Array Size':>12} | {'Selection Sort':>15} | {'Bubble Sort':>12} | "
          f"{'Insertion Sort':>15} | {'Merge Sort':>10} | {'Quick Sort':>10}")
    print("-" * 80)

    for size in array_sizes:
        row = timing_results[size]
        print(f"{size:>12} | {row['Selection Sort']:>15.5f} | {row['Bubble Sort']:>12.5f} | "
              f"{row['Insertion Sort']:>15.5f} | {row['Merge Sort']:>10.5f} | "
              f"{row['Quick Sort']:>10.5f}")

    print("=" * 80)

if __name__ == "__main__":
    main()
