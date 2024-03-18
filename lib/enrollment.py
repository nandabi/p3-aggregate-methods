from datetime import datetime

class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, course):
        if isinstance(course, Course):
            enrollment = Enrollment(self, course)
            self._enrollments.append(enrollment)
            course.add_enrollment(enrollment)
            self._grades[enrollment] = None  # Initialize grade as None
        else:
            raise TypeError("course must be an instance of Course")

    def get_enrollments(self):
        return self._enrollments.copy()

    def course_count(self):
        return len(self._enrollments)

    def set_grade(self, enrollment, grade):
        if enrollment in self._grades:
            self._grades[enrollment] = grade
        else:
            raise ValueError("Invalid enrollment")

    def aggregate_average_grade(self):
        total_grades = sum(grade for grade in self._grades.values() if grade is not None)
        num_courses = sum(1 for grade in self._grades.values() if grade is not None)
        if num_courses == 0:
            return 0  # Avoid division by zero
        average_grade = total_grades / num_courses
        return average_grade


class Course:
    def __init__(self, title):
        self.title = title
        self._enrollments = []

    def add_enrollment(self, enrollment):
        if isinstance(enrollment, Enrollment):
            self._enrollments.append(enrollment)
        else:
            raise TypeError("enrollment must be an instance of Enrollment")

    def get_enrollments(self):
        return self._enrollments.copy()


class Enrollment:
    all = []

    def __init__(self, student, course):
        if isinstance(student, Student) and isinstance(course, Course):
            self.student = student
            self.course = course
            self._enrollment_date = datetime.now()
            type(self).all.append(self)
        else:
            raise TypeError("Invalid types for student and/or course")

    def get_enrollment_date(self):
        return self._enrollment_date

    @classmethod
    def aggregate_enrollments_per_day(cls):
        enrollment_count = {}
        for enrollment in cls.all:
            date = enrollment.get_enrollment_date().date()
            enrollment_count[date] = enrollment_count.get(date, 0) + 1
        return enrollment_count
