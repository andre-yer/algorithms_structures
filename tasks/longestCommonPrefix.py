class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ''
        shortest = min(strs, key=len)
        for i, value in enumerate(shortest):
            for item in strs:
                if item[i] != value:
                    return shortest[:i]
        return shortest


def main():
    strs = list(input().split())
    pref = Solution()
    print(pref.longestCommonPrefix(strs))


if __name__ == '__main__':
    main()
