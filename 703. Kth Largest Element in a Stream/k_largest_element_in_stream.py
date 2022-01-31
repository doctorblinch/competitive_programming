from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if not self.nums:
            self.nums = [val]

        l = 0
        r = len(self.nums) - 1

        while True:
            if self.nums[r] <= val:
                self.nums.insert(r+1, val)
                break
            elif self.nums[l] >= val:
                self.nums.insert(l, val)
                break

            middle = l + (r - l) // 2
            if middle == l:
                self.nums.insert(r, val)
                break
            # if self.nums[middle] <= val <= self.nums[middle+1]:

            if self.nums[middle] <= val:
                l = middle
            else:
                r = middle

        if len(self.nums) > self.k:
            self.nums.pop(0)
        return self.nums[0]


nums = list(range(10))  # [4, 5, 8, 2]
nums = [0]
k = 2
val = -1
# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(k, nums)
param_1 = obj.add(val)
print(obj.nums)
