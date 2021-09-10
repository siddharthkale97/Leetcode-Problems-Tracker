class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.paths = []
        def ct(curr, newtarget,candidates,path):
            if newtarget == 0:
                self.paths.append(path)
                return True
            elif newtarget<0:
                return False
            else:
                for i in range(curr,len(candidates)):
                    newnewtarget = newtarget - candidates[i]
                    temppath = path[:]
                    temppath.append(candidates[i])
                    ct(i, newnewtarget,candidates,temppath)
            return
        path = []
        ct(0,target,candidates, path)
        #print(self.paths)
        return self.paths
                