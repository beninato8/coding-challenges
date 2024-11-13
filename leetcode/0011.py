class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(a, b):
            return (b - a) * min(height[a], height[b])
        a = 0
        b = len(height) - 1
        biggest = area(a, b)
        while a < b:
            if height[a] < height[b]:
                a += 1
            else:
                b -= 1
            if area(a, b) > biggest:
                biggest = area(a, b)
        return biggest
        
