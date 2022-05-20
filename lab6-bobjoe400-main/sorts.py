import random
import time

def selection_sort(list):
    comp = 0
    def swap(list, i, j):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp

    for i in range(len(list) - 1):
        min_spot = i
        for j in range(i+1, len(list)):
            comp+=1
            if list[j] < list[min_spot]:
                min_spot = j
        if i != min_spot:
            swap(list, i, min_spot)
    return comp

def insertion_sort(list):
    k = 0
    n = len(list) - 1
    comparisons = 0
    while k+1 <= n:
        i = k+1
        curr_val = list[i]
        comparisons += 1
        while i>0 and list[i-1] > curr_val:
            list[i] = list[i-1]
            i=i-1
            comparisons += 1
        list[i] = curr_val
        k = k + 1
    return comparisons

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    sizes = [1,2,4,8,16,32]
    for i in sizes:
        randoms = random.sample(range(1000000), i*1000)
        start_time = time.time()
        comps = selection_sort(randoms)
        #comps = insertion_sort(randoms)
        stop_time = time.time()
        print('s_s %d'%(i*1000),comps, stop_time - start_time)

if __name__ == '__main__':
    main()

