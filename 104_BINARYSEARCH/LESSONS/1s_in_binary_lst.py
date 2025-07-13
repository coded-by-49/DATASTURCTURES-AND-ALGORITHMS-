'''Given a binary array arr[] of size N, which is sorted in non-increasing order, count the number of 1's in it. '''

def First_or_last_occurences(nums:list,first_occurence:bool):
    answer = -1
    start = 0
    end = len(nums)-1 
    while start <= end:
        mid = start + (end - start)//2
        if nums[mid] < 1:
            end = mid - 1
        else: 
            answer = mid 
            if first_occurence:
                end = mid - 1
            else:
                start = mid + 1
    return answer

if __name__ == "__main__":
    bins = [1,0,0]
    last = First_or_last_occurences(bins,False)
    first = First_or_last_occurences(bins,True)

    if last != -1 and first != -1:
        print(last-first + 1)
    else:
        print(0)
