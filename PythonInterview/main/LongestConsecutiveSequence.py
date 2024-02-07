def longestConsecutive(a):
    print(a)
    a = set(a) # Converting into Set to avoid Duplicates
    print(a)
    longest = 0
    for i in a:
        print("For : ", i)
        if i - 1 not in a:
            print("If :" , i)
            streak = 0
            while i in a:
                print("In While :  ", i)
                i += 1
                streak += 1
                longest = max(longest, streak)
        else:
            print(" Previous number found for ", i)
    return longest



print(longestConsecutive([100, 4, 250, 1, 3, 2,5,5]))