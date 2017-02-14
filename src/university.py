class University(object):

    def __init__(self, name):
        self.name = name
        self.colleges = []

    def add_colleges(self, name):
        college = College(name)
        self.colleges.append(college)
        print("College added")
        return college

    def update(self):
        #print([str(college) for college in University.colleges])
        for college in self.colleges:
            print([str(college)])
            for department in college.departments:
                print([str(department)])


class College(object):

    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = []

    def add_department(self,name):
        department = Department(name)
        self.departments.append(department)
        print("Department added")
        return department

    def view_students(self):
        for student in self.students:
            print([str(student)])

    def add_student(self,student):
        self.students.append(student)

    def __str__(self):
        return "College name: {}".format(self.name)


class Department(object):

    def __init__(self, name):
        self.name = name
        self.course_schedule_list = []

    def __str__(self):
        return "Department name: {}".format(self.name)

    def add_course_catalog(self,catalog):
        self.course_catalog = catalog

    def add_course_schedule(self, course_schedule):
        self.course_schedule_list.append(course_schedule)

    def view_course_catalog(self):
        for course in course_catalog.courses:
            print([str(course)])

    def view_course_offering(self):
        for course_schedule in self.course_schedule_list:
            print([str(course_schedule)])
            for course_offering in course_schedule.course_offerring:
                print([str(course_offering)])


class Semester(object):
    terms = [
        "Fall 2015",
        "Spring 2016",
        "Summer 2016",
        "Fall 2016"
    ]

    @staticmethod
    def add_terms(self, name):
        Semester.terms.append(name)


class CourseSchedule(object):

    terms = [
         "Fall 2015",
         "Spring 2016",
         "Summer 2016",
         "Fall 2016"
    ]

    def __init__(self, semester):
      self.semester = self.terms[semester]
      self.course_offerring = []

    def __str__(self):
      return "Course offered for Semester: {}".format(self.semester)


class CourseOffering(object):

    ref = 1;

    def __init__(self, course, professor, total_seats):
        self.course = course
        self.professor = professor
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.schedule = {}
        self.seats = []

    def assign_seat(self):
        seat = Seats("Assigned")
        self.seats.append(seat)
        return seat



    def __str__(self):
      return "Course Name: {}|| Course Professor: {} || Available seats: {} ".format(self.course.name, self.professor, self.available_seats)




class Seats(object):

    seat_no = 1

    def __init__(self, status):
        self.status = status
        Seats.seat_no += 1


class Transcript(object):

    def __init__(self):
        self.course_load_list = []

    def add_course_load(self,semester):
        course_load = CourseLoad(semester)
        self.course_load_list.append(course_load)
        return course_load


class CourseLoad(object):

    def __init__(self, semester):
        self.semester = Semester.terms[semester]
        self.seat_assignments = []

    def add_seat_assignment(self):
        seat_assignment = SeatAssignment()
        self.seat_assignments.append(seat_assignment)
        return seat_assignment

class SeatAssignment(object):

    def __int__(self):
        print "assigned seat"
        self.grade = "Not Set"

    def add_grade(self, grade):
        self.grade = grade

    def assign_seat_to_student(self, seat):
        self.seat = seat


class CourseCatalog(object):

    def __init__(self):
        print "Adding course catalog"
        self.courses = []

    def add_courses(self, course):
        course = Course(course)
        self.courses.append(course)
        return course

class Course(object):

    course_id = 1

    def __init__(self, name):
        self.course_id = Course.course_id
        self.name = name
        Course.course_id += 1

    def __str__(self):
        return "Course ID : {} || Course Name: {}".format(self.course_id, self.name)


class Student(object):

    count = 1

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.id = self.count
        Student.count += 1
        self.transcript = Transcript()

    def view_grades_by_sem(self):
        transcript = self.transcript
        print("Found transcript")
        for course_load in transcript.course_load_list:
            print("Semester registered for {}".format(course_load.semester))


    def __str__(self):
        return "Student ID: {}, Student Name{}, {}".format(self.id, self.last_name,self.first_name)


if __name__ == "__main__":
    x = University("Northeastern")
    c1 = x.add_colleges("COE")
    c2 = x.add_colleges("Business")
    department = c1.add_department("Information Systems")
    course_catalog = CourseCatalog()
    course1 = course_catalog.add_courses("DBMS")
    course2 = course_catalog.add_courses("Web Design")
    department.add_course_catalog(course_catalog)

    print("Iterating the list")
    department.view_course_catalog()
    cs1 = CourseSchedule(0)
    co1 = CourseOffering(course1,"Yusuf Ozbek",40)
    co2 = CourseOffering(course2,"Chaiya",20)
    cs1.course_offerring.append(co1)
    cs1.course_offerring.append(co2)
    department.course_schedule_list.append(cs1)
    department.view_course_offering()
    print("Adding students")
    s1 = Student("Bhavna", "Menghrajani")
    s2 = Student("Pooja", "Chainani")
    c1.add_student(s1)
    c1.add_student(s2)
    c1.view_students()
    cL = s1.transcript.add_course_load(0)
    seat = co1.assign_seat()
    seat_assignment = cL.add_seat_assignment()
    seat_assignment.add_grade("A")
    seat_assignment.assign_seat_to_student(seat)
   # cl = s1.transcript.add_course_load(0)
    s1.view_grades_by_sem()
    print("Viewing course offering to student 1")

    x.update()




