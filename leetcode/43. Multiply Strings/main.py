class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = ''
        remain = 0

        for i in range(1, max(len(num1), len(num2)) + 1):
            result += str(
                int(num1[-i]) if len(num1) <= i else 1 * int(num2[-i])
            )


solution = Solution()
print(solution.multiply('2', '3'))
