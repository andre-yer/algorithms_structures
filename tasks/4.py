from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # simple solution
        # new_num = sorted(nums1 + nums2)
        # if len(new_num) % 2 == 1:
        #     return float(new_num[len(new_num) // 2])
        # else:
        #     return (new_num[len(new_num) // 2] + new_num[len(new_num) // 2 - 1]) / 2

        new_num = []
        i, j = 0, 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] < nums2[j]:
                new_num.append(nums1[i])
                i += 1
            else:
                new_num.append(nums2[j])
                j += 1
        while (i < len(nums1)):
            new_num.append(nums1[i])
            i += 1
        while (j < len(nums2)):
            new_num.append(nums2[j])
            j += 1
        if len(new_num) % 2 == 1:
            return float(new_num[len(new_num) // 2])
        else:
            return (new_num[len(new_num) // 2] + new_num[len(new_num) // 2 - 1]) / 2


def main():
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    solution = Solution()
    print(solution.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    main()
