class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        visited = set()
        
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre, in prerequisites:
            preMap[crs].append(pre)
            
        print(preMap)
        
        preMap1 = {}   
        for i in range(len(prerequisites)):
            course = prerequisites[i][0]
            prereq = prerequisites[i][1]
            
            if course not in preMap1:
                preMap1[course] = []
            
            preMap1[course].append(prereq)
        print(preMap1)
        
        def dfs(course):
         
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre): return False
            
            visited.remove(course)
            preMap[course] = []
            return True
           
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True