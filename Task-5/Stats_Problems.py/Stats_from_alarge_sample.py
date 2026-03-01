from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = maximum = -1
        total = 0
        total_sum = 0
        mode = 0
        
        for k in range(256):
            if count[k] > 0:
                if minimum == -1:
                    minimum = k
                maximum = k
                total += count[k]
                total_sum += k * count[k]
                if count[k] > count[mode]:
                    mode = k
        
        mean = total_sum / total

        running = 0
        median1 = median2 = None
        odd = total % 2 == 1
        mid1 = total // 2
        mid2 = mid1 if odd else mid1 - 1
        
        for i in range(256):
            running += count[i]
            if median2 is None and running > mid2:
                median2 = i
            if median1 is None and running > mid1:
                median1 = i
                break
        
        median = (median1 + median2) / 2

        return [float(minimum), float(maximum), mean, median, float(mode)]