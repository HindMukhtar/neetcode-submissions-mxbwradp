class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        # BF Solution 
        # use a heap and store top k based on difference between val and x 
        # max heap with top k min distances 
        # heap push - O(logn) and repeat n times so O(nlogn)
        # then need to return in ascending order so will have to pop from heap 
        # and reverse - overall ~ O(nlogn)

        # but the list is sorted, so can we do better? 
        # sliding window of size k 
        # if len of sliding window > k we make a choice to either remove from back 
        # and add from front, or we exit the loop. Because array is sorted, if current 
        # value is already worse than previous values, then tehres no need to coninute 
        # searching 
        # This solution is O(n) time and O(1) space 

        l = 0 
        r = len(arr) - 1 

        while r-l+1 > k: 

            if abs(arr[l] - x) <= abs(arr[r] - x): 
                r -= 1
            else: 
                l += 1 

        return arr[l:r+1]
