class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par_dict = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in par_dict:
                top_stack = stack.pop() if stack else '?'
                if top_stack != par_dict[char]:
                    return False
            else:
                stack.append(char)
        return not stack


def main():
    print(Solution().isValid('()[]{}'))
    print(Solution().isValid('([)]'))
    print(Solution().isValid('{[]}'))


if __name__ == '__main__':
    main()
