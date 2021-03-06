import time

# stopped it after 30 mins or so without an answer
# need a new approach
def lexicographic(nums, nth):
    found=0
    numstr=("").join(map(str,nums)).zfill(10)
    current=int(("").join(map(str,nums)))
    while found<nth:
        check = "".join(sorted(str(current).zfill(10)))
        if numstr==check:
            found+=1
        current+=1
    return current

def get_next(nums):
    # find longest subsection that won't increase (highest permutation)
    i = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i-=1
    # now i is the start of the subsection

    #are we at the front
    if i<=0:
        print "Last permutation reached."
        return nums

    # let nums[i-1] be the next to move
    # find the rightmost element that is bigger than num[i-1]
    j =  len(nums)-1
    while nums[j] <= nums[i-1]:
        j-=1
    # now the value of nums[j] becomes the new number to move
    # assertion: j >= i

    # swap the number with j
    temp = nums[i-1]
    nums[i-1] = nums[j]
    nums[j] = temp

    # reverse the subsection to have from lowest to highest
    j = len(nums)-1
    while i<j:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        i+=1
        j-=1
    return nums       
    
def lexic(nums, nth):
    start = time.time()
    for i in xrange(1,nth):
        nums = get_next(nums)
    print "Time taken to complete: %r secs." % (time.time() - start)
    return nums

def permutations_possible(nums,printit=False):
    # there are 10 digits, so 10! different combinations of answers
    current=1
    last=[1]
    while True:
        nums = get_next(nums)
        if printit: print nums
        if last==nums:
            print "Exiting"
            break
        last=nums[:]
        current+=1
    return current

if __name__=="__main__":
    print lexic([0,1,2,3,4,5,6,7,8,9], 1000000)
    # [2, 7, 8, 3, 9, 1, 5, 4, 6, 0]
    # 0.9446179866790771 secs
    assert permutations_possible([0,1,2], True)==6
    assert permutations_possible([0,1,2,3,4,5,6,7,8,9])==3628800
    

