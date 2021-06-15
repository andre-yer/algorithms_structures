class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            max_substr = 0
        else:
            max_substr = 1
        for i in range(len(s)):
            substr = 0
            for j in range(i, len(s)):
                if s[j] not in s[i:j]:
                    substr += 1
                    if substr > max_substr:
                        max_substr = substr
                else:
                    break
        return max_substr


def main():
    s = input()
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()
