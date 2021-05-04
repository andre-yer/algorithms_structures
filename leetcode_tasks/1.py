from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], i]
            index[x] = i


def main():
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    print(solution.twoSum(nums, target))


if __name__ == '__main__':
    main()
