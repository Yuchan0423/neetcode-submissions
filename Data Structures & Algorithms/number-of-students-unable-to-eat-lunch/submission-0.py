class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = 0 
        count = len(sandwiches)
        while i < len(sandwiches) and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                i = 0
                count -= 1
            else:
                student_preference = students.pop(0)
                students.append(student_preference)
                i += 1
        
        return count
                