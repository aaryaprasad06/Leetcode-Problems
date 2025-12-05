class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c0= students.count(0)
        c1= students.count(1)
        for i in sandwiches:
            if i==0:
                if c0==0:
                    return c1
                c0-=1 
            else:
                if c1==0:
                    return c0 
                c1-=1 
        return 0