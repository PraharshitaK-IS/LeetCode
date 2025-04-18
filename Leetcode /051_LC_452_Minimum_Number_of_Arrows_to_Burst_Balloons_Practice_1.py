class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Step 1: Sort by end coordinate
        points.sort(key=lambda x: x[1])

        arrows = 1
        current_end = points[0][1]

        for start, end in points[1:]:
            # If current balloon starts after the last arrow's position
            if start > current_end:
                arrows += 1
                current_end = end  # update arrow to new balloon's end

        return arrows
