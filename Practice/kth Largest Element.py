import heapq
def find_kth_largest(test_arr, k):
    # Initialize a new heap array
    heap_arr = []
    # heapq.heapify(heap_arr)

    # Loop through the test array
    for i in range(len(test_arr)):
        # Check if the initial k elements have been added to the heap
        if len(heap_arr) < k:
            heapq.heappush(heap_arr, test_arr[i])

        else:
            # Check if we have found a larger element
            if heap_arr[0] > test_arr[i]:
                continue
            heapq.heappop(heap_arr)
            heapq.heappush(heap_arr, test_arr[i])
    return heap_arr[0]


# Test cases
arr = [3, 2, 1, 5, 6, 4]
print(find_kth_largest(arr, 6))
