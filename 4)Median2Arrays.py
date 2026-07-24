# [1,2,3]

def findMedianSortedArrays(nums1, nums2):
        nums = sorted(nums1 + nums2)
        if len(nums)%2==0:
            return (nums[len(nums)//2-1]+nums[len(nums)//2])/2.0
        else:
            return (nums[len(nums)//2])
    
print(findMedianSortedArrays([1,2],[3,4]))