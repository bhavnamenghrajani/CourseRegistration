class University(object):

    """" A root class storing university related information
    Attributes:
        name : name of the university
        colleges[] : list of colleges for a university
    """

    def __init__(self, name):
        """"Initialize university name and an empty list to store college details"""
        self.name = name
        self.colleges = []

    def add_colleges(self, name):
        """"Perform operation to create a new college instance and append it to the colleges list"""
        college = College(name)
        self.colleges.append(college)
        print("College added")
        return college

    def retrieve_college_details(self):
        """"Retrieves college details along with the department associated with it"""
        for college in self.colleges:
            print([str(college)])
            for department in college.departments:
                print([str(department)])


class College(object):
    """"
        A class storing individual college details
        Attributes:
            name: name of the college
            departments[]: list of departments associates with a college
    """
    def __init__(self, name):
        """" Initializes collge name, department and student list"""
        self.name = name
        self.departments = []
        self.students = []

    def add_department(self,name):
        """"Adds a department to the college"""
        department = Department(name)
        self.departments.append(department)
        print("Department added")
        return department

    def view_students(self):
        """"Retrieves student details"""
        for student in self.students:
            print([str(student)])

    def add_student(self,student):
        """"Add students to the department"""
        self.students.append(student)

    def __str__(self):
        """"Format to display College"""
        return "College name: {}".format(self.name)


class Department(object):
    """"
        A class to store department related information
        Attributes:
            name: name of the department
            course_schedule_list: stores the schedule of the courses offered by department by semester
            course_catalog: stores the list of courses which the department is entitled to offer
    """
    def __init__(self, name):
        """ Initializes the name of department and course catalog list"""
        self.name = name
        self.course_schedule_list = []

    def __str__(self):
        return "Department name: {}".format(self.name)

    def add_course_catalog(self,catalog):
        """"Adds the course to the catalog"""
        self.course_catalog = catalog

    def add_course_schedule(self, course_schedule):
        """"Add the course schedule to the list"""
        self.course_schedule_list.append(course_schedule)

    def view_course_catalog(self):
        """"Retrieve the course from the catalog"""
        for course in course_catalog.courses:
            print([str(course)])

    def view_course_offering(self):
        """"Retrieve the schedule of courses offered"""
        for course_schedule in self.course_schedule_list:
            print([str(course_schedule)])
            for course_offering in course_schedule.course_offerring:
                print([str(course_offering)])


class Semester(object):
    """"Class to store the static content"""

    terms = [
        "Fall 2015",
        "Spring 2016",
        "Summer 2016",
        "Fall 2016"
    ]

    @staticmethod
    def add_terms(self, name):
        """"To add the contents in list : terms"""
        Semester.terms.append(name)


class CourseSchedule(object):
    """"Associate a schedule to store the courses offered per semester"""
    terms = [
         "Fall 2015",
         "Spring 2016",
         "Summer 2016",
         "Fall 2016"
    ]

    def __init__(self, semester):
      """"Assign semester to the schedule and initialize the course offering list"""
      self.semester = self.terms[semester]
      self.course_offerring = []

    def __str__(self):
      return "Course offered for Semester: {}".format(self.semester)


class CourseOffering(object):
    """Class to store the details about class being taught in a given semester
        Attributes:
            course: course object
            professor: name of the professor
            total_seats: the total number of seats for the course offered
            avaialble_seats: the remaining seats
            schedule: dictionary to store the schedule for Day and Time of a Week
            seats: the seat related information
    """
    ref = 1;

    def __init__(self, course, professor, total_seats):
        self.course = course
        self.professor = professor
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.schedule = {}
        self.seats = []

    def assign_seat(self):
        """"Adds seat to the seats list"""
        seat = Seats("Assigned")
        self.seats.append(seat)
        return seat



    def __str__(self):
      return "Course Name: {}|| Course Professor: {} || Available seats: {} ".format(self.course.name, self.professor, self.available_seats)




class Seats(object):
    """"A class to store the seat related information
        Attributes:
            seat_no: A unique number for seat
            status: A status of a seat
    """
    seat_no = 1

    def __init__(self, status):
        """"Intialize the status of seat"""
        self.status = status
        Seats.seat_no += 1


class Transcript(object):
    """A class to store the overall gpa of a student
        Attributes:
            course_load_list : List to store the term wise courses taken by student
    """
    def __init__(self):
        self.course_load_list = []

    def add_course_load(self,semester):
        """Adds a course load - semester wise courses opted by student"""
        course_load = CourseLoad(semester)
        self.course_load_list.append(course_load)
        return course_load


class CourseLoad(object):
    """"A class that store courses being taken by a stident in a Semester
        Attributes:
            semester: determine the semester or term
            seat_assignments[]: list of individual course registered
    """
    def __init__(self, semester):
        """Initializes course and seat assignment list"""
        self.semester = Semester.terms[semester]
        self.seat_assignments = []

    def add_seat_assignment(self):
        """Append a seat_assignment to the list- seat_assignments"""
        seat_assignment = SeatAssignment()
        self.seat_assignments.append(seat_assignment)
        return seat_assignment

class SeatAssignment(object):
    """"A class to store the individual seat assigned - the seat of a course and the grade
        Attributes:
            grade: grade received in a course
            seat: a seat of a course
    """
    def __int__(self):
        print "assigned seat"
        self.grade = "Not Set"

    def add_grade(self, grade):
        """Add grade to the seat_assignemnt"""
        self.grade = grade

    def assign_seat_to_student(self, seat):
        """"Associate seat of a course to the student seat_assignment"""
        self.seat = seat


class CourseCatalog(object):
    """"A class to store the list of courses
        Attributes:
            courses[]: list of course
    """
    def __init__(self):
        print "Adding course catalog"
        self.courses = []

    def add_courses(self, course):
        """"Adds courses to the course_list"""
        course = Course(course)
        self.courses.append(course)
        return course

class Course(object):
    """"
        A class to store the course details
        Attributes:
            course_id: A unique id for the course
            name: A name of a course
    """
    course_id = 1

    def __init__(self, name):
        """"Initialize course id and course name"""
        self.course_id = Course.course_id
        self.name = name
        Course.course_id += 1

    def __str__(self):
        return "Course ID : {} || Course Name: {}".format(self.course_id, self.name)


class Student(object):
    """A class to store the student details
        Attributes:
            first_name: First name of a student
            last_name: Last name of a student
            id: a unique id a student
            transcript: A Transcript for a student
    """
    count = 1

    def __init__(self, first_name, last_name):
        """"Initialize the first name, last name, id, transcript"""
        self.first_name = first_name
        self.last_name = last_name
        self.id = self.count
        Student.count += 1
        self.transcript = Transcript()

    def view_grades_by_sem(self):
        """"To view the grades of a student"""
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
    s1.view_grades_by_sem()
    print("Viewing course offering to student 1")
    x.retrieve_college_details()




