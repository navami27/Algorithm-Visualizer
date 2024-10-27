def swap(li, i, j):
	if i != j:
		li[i], li[j] = li[j], li[i]

def BubbleSort(li):
	swapped = False #flag in case if list is already sorted.
	for i in range(len(li) - 1):
		for j in range(len(li) - 1 - i):
			if li[j] > li[j + 1]:
				swap(li, j, j+1)
				swapped = True
				yield li #so that any update in data can be visualized at each iteration.
		if not swapped:  #when list is already sorted.
			break

def MergeSort(li, low, high):
	if high <= low:
		return
	mid = (low+high)//2
	yield from MergeSort(li, low, mid)
	yield from MergeSort(li, mid+1, high)
	yield from merge(li, low, mid, high)
	yield li

def merge(li, low, mid, high):
	merged_li = []
	left_start = low
	right_start = mid+1
	# going through two chunks of data and merging on sort.
	while left_start <= mid and right_start <= high:
		if li[left_start] < li[right_start]:
			merged_li.append(li[left_start])
			left_start += 1
		else:
			merged_li.append(li[right_start])			
			right_start += 1
	# for remaining elements from left chunk
	while left_start <= mid:
		merged_li.append(li[left_start])
		left_start += 1
	# for remaining elements from right chunk
	while right_start <= high:
		merged_li.append(li[right_start])
		right_start += 1
	for i, j in enumerate(merged_li):
		li[low + i] = j
		yield li

def InsertionSort(li):
	for i in range(1, len(li)):
		j = i
		while j > 0 and li[j] < li[j-1]:
			swap(li, j, j-1)
			j -= 1
			yield li

def QuickSort(li, start, end):
    if start >= end:
        return
    pivot = li[end]
    pivotIdx = start
    for i in range(start, end):
        if li[i] < pivot:
            swap(li, i, pivotIdx)
            pivotIdx += 1
        yield li
    swap(li, end, pivotIdx)
    yield li
    yield from QuickSort(li, start, pivotIdx - 1)
    yield from QuickSort(li, pivotIdx + 1, end)
def ShellSort(li):
    n = len(li)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = li[i]
            j = i
            while j >= gap and li[j - gap] > temp:
                li[j] = li[j - gap]
                j -= gap
            li[j] = temp
        gap //= 2
        yield li
def cycleSort(li):
    writes = 0
    n = len(li)
    for cycleStart in range(n - 1):
        item = li[cycleStart]
        pos = cycleStart
        for i in range(cycleStart + 1, n):
            if li[i] < item:
                pos += 1
        if pos == cycleStart:
            continue
        while item == li[pos]:
            pos += 1
        li[pos], item = item, li[pos]
        writes += 1
        yield li
        while pos != cycleStart:
            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if li[i] < item:
                    pos += 1
            while item == li[pos]:
                pos += 1
            li[pos], item = item, li[pos]
            writes += 1
            yield li
    return writes
def timSort(li):
    min_run = 32
    n = len(li)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        yield from InsertionSort(li)

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            yield from merge(li, left, mid,right )
        size = 2 * size
def cocktail_sort(li):
    n = len(li)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Move from left to right (forward)
        for i in range(start, end):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                swapped = True
                yield li

        if not swapped:
            break

        swapped = False
        end -= 1

        # Move from right to left (backward)
        for i in range(end - 1, start - 1, -1):
            if li[i] > li[i + 1]:
                li[i], li[i + 1] = li[i + 1], li[i]
                swapped = True
                yield li

        start += 1

    



    


        

