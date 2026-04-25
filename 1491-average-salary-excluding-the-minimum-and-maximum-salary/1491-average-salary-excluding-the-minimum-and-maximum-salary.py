class Solution:
    def average(self, salary: List[int]) -> float:
        mod=10**(-5)
        salary.sort()
        n=len(salary)-2
        total=0
        for i in range(1,len(salary)-1):
            total+=salary[i]
        res=(total/n)
        return res
        