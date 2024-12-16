class SearchStudent:
    def __init__(self, student_info):
        self.student_info = student_info

    def search_by_id(self, student_id):
        """Searches for a student by ID."""
        for student in self.student_info.allstudents:
            if student.getIDNum() == student_id:
                return student
        return None
