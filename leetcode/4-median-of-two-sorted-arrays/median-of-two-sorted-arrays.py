class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
    
        n,m=len(nums1),len(nums2)
        i,j=0,0
        result=[]
        while i<n and j<m:
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        
        if i<n:
            while i<n:
                result.append(nums1[i])
                i+=1
        if j<m:
            while j<m:
                result.append(nums2[j])
                j+=1
        
        mid=len(result)//2
        if mid==len(result)/2:
            return (result[mid]+result[mid-1])/2
        else:
            return result[mid]

    
    