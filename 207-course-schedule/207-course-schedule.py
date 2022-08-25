class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        traced = set()
        visit = set()
        def dfs(crs):
            if crs in traced: return False
            if crs in visit: return True
            
            traced.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            traced.remove(crs)
            visit.add(crs)
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
                
            
        
        
            