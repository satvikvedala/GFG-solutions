class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def func(candidates,target,su,temp,res,index):
            if su>target:
                return
            if su == target:
                res.append(temp.copy())
                return
            else:
                for i in range(index,len(candidates)):
                    temp.append(candidates[i])
                    func(candidates,target,su+candidates[i],temp,res,i)
                    temp.pop()
            
        res = []
        func(candidates,target,0,[],res,0)
        return res
