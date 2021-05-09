def number_of_good_pairs(nums):
    # keep track of my good pairs
    # iterate over the nums using a nested loop, using i and j as the indices
    # check if the nums at i are thes same as the nums at j
    # if that is the case then increment the good pairs
    # once the loops are finished return the good pairs to the caller
    
    # first pass solution (brute force) O(n^2) Quadratic runtime
    good_pairs = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                good_pairs += 1
    
    return good_pairs


print(number_of_good_pairs([1,2,3,1,1,3])) # => 4
                    