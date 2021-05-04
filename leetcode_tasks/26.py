from typing import List 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        orig = 0
        for i in range(len(nums)):
            if nums[orig] != nums[i]:
                orig += 1
                nums[orig] = nums[i]
        return orig + 1


def main():
    nums = list(map(int, input().split()))
    duplicate = Solution()
    print(duplicate.removeDuplicates(nums))


if __name__ == '__main__':
    main()
