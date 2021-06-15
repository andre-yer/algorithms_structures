class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        result, prev = 0, 0
        for item in s[::-1]:
            if roman_dict[item] >= prev:
                result += roman_dict[item]
            else:
                result -= roman_dict[item]
            prev = roman_dict[item]
        return result


def main():
    print(Solution().romanToInt('MMXXI'))


if __name__ == '__main__':
    main()
