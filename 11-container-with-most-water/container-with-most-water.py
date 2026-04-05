class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        left, right = 0, len(height) - 1

        while left < right:
            h = min(height[left], height[right])
            width = right - left
            maxA = max(maxA, h * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA