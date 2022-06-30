// https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre_map = defaultdict(list)
        for course in range(numCourses):
            pre_map[course]
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)
        visited = set()
        valid = set()
        
        def dfs(course):
            
            if course in visited:
                return False
            if len(pre_map[course]) == 0 or course in valid:
                valid.add(course)
                return True
            
            visited.add(course)
            
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            valid.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True