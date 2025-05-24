#https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Initialize queue with nodes having in-degree 0 (no prerequisites)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0

        # Step 3: Process courses
        while queue:
            current = queue.popleft()
            count += 1
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses were processed
        return count == numCourses
