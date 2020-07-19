class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr)==0 or len(arr)==1:
            return []
        
        arr.sort()
        for i in range(len(arr)):
            for j in range(i):
                if arr[j]*2 ==arr[i] or arr[i]*2 == arr[j]:
                    return 1
