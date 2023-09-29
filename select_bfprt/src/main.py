from algorithms.select_bfprt import SelectBFPRT

if __name__ == '__main__':
    median_of_medians = SelectBFPRT([1, 6, 2, 5, 4], 5)
    print(median_of_medians.find_kth_smallest(3))
