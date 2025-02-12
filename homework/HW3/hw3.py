import random as rand
import time


def generate_lists(size):
    L1 = rand.sample(range(size * 2), size)
    L2 = rand.sample(range(size * 2), size)
    return L1, L2


def find_common(list1, list2):
    """
    Uses brute force to find every match, comparing one number in list one to everynumber in list two before moving onto the next number O(N^2)
    Args:
        list1, list2 (int): random number of ints based off of generate_list(size)
    Returns:
        int: how many of the same numbers are there in the list
    """
    common_items = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                common_items += 1
    return common_items


def find_common_efficient(list1, list2):
    """
    Sorts our lists, in acending order. Then uses a two pointer approach to find the number of common_items in O(N) time
    Args:
        list1, list2 (int): random number of ints based off of generate_list(size)
    Returns:
        int: how many of the same numbers are there in the list
    """
    list1.sort()
    list2.sort()
    common_items = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            common_items += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return common_items


def measure_time():
    """
    Measures and compares the execution time of two functions, `find_common` and
    `find_common_efficient`, which determine common elements between two lists.

    Output:
    - Prints a table displaying the list size, time taken by `find_common`, and time
      taken by `find_common_efficient`.
    """
    sizes = [10, 100, 1000, 10000, 20000]

    results = []

    for size in sizes:
        L1, L2 = generate_lists(size)

        start_time = time.perf_counter()
        x = find_common(L1, L2)
        time_find_common = time.perf_counter() - start_time

        L1, L2 = generate_lists(size)

        start_time = time.perf_counter()
        y = find_common_efficient(L1, L2)
        time_find_common_efficient = time.perf_counter() - start_time

        results.append((size, time_find_common, time_find_common_efficient))

    print(f"{'Size':<10}{'Brute Force Time (s)':<25}{'Efficient Time (s)':<25}")
    print("=" * 60)
    for size, time_find_common, time_find_common_efficient in results:
        print(f"{size:<10}{time_find_common:<25}{time_find_common_efficient:<25}")


measure_time()
