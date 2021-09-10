class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.visited = set()
        q = []
        q.append(0)
        while (len(q)>0):
            if len(nums)-1 in self.visited:
                return True
            node = q.pop(0)
            self.visited.add(node)
            for i in range(0,nums[node]):
                q.append(i+node+1)
        return False