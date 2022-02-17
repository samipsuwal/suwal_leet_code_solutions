class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans=[0]*(m+n)
    
        copy_nums1 = nums1[0:m]

        left = 0
        right = 0

        for i in range(m+n):
            if left>m-1:
                ans[i] = nums2[right]
                right+=1
                continue
            elif right> n-1:
                ans[i] = copy_nums1[left]
                left+=1
                continue

            if nums1[left] < nums2[right]:
                ans[i] = copy_nums1[left]
                left +=1
            else:
                ans[i] = nums2[right]
                right +=1

        for i in range(m+n):
            nums1[i] = ans[i]
        