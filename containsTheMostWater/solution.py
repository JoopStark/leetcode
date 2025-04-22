class Solution():
    def maxArea(self, height: list[int]) -> int:
        left_pointer = 0
        right_pointer = len(height) - 1

        max_volume = 0

        while left_pointer < right_pointer:
            min_pointer = min(height[left_pointer], height[right_pointer])
            temp_max = (right_pointer - left_pointer) * min_pointer
            if max_volume < temp_max:
                max_volume = temp_max
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_volume
