from typing import List
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list and in-degree list
        adjacency_list = defaultdict(list)
        in_degree = [0] * numCourses

        for course, pre in prerequisites:
            adjacency_list[pre].append(course)
            in_degree[course] += 1
        
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        course_taken = 0

        while q:
            course = q.popleft()
            course_taken += 1

            for next_course in adjacency_list[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return course_taken == numCourses


"""
Complexity:
- Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
- Space Complexity: O(V + E), for the adjacency list and in-degree array.
"""