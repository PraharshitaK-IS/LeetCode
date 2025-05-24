
#https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Step 2: Add all courses with no prerequisites to queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        order = []

        # Step 3: Process courses in topological order
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if all courses are included
        if len(order) == numCourses:
            return order
        else:
            return []  # Cycle detected
            