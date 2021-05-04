class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        been_dict = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            if s[right] not in been_dict:
                longest = max(longest, right - left + 1)
            else:
                if been_dict[s[right]] < left:
                    longest = max(longest, right - left + 1)
                else:
                    left = been_dict[s[right]] + 1
            been_dict[s[right]] = right
        return longest


def main():
    s = input()
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
