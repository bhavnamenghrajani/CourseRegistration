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

    def __init__(self, semester):
      """"Assign semester to the schedule and initialize the course offering list"""
      self.course_offerring = []
      try :
        self.semester = Semester.terms[semester]
      except IndexError:
          print "The term has not been set"



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
        if self.available_seats > 0:
            seat = Seats("Assigned")
            self.seats.append(seat)
            self.available_seats -= 1
            return seat
        else:
            print "No more seats are available"

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

    def add_course_offering(self, course_offering):
        self.course_offering = course_offering


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
        try :
            self.semester = Semester.terms[semester]
            self.seat_assignments = []
        except IndexError:
            print "Term has not been set"

    def add_seat_assignment(self):
        """Append a seat_assignment to the list- seat_assignments"""
        seat_assignment = SeatAssignment()
        self.seat_assignments.append(seat_assignment)
        return seat_assignment

    def drop_seat_assignment(self,seat_assignment):
        seat_old = seat_assignment.seat
        course_offered = seat.course_offering
        course_offered.seats.remove(seat_old)
        course_offered.available_seats += 1
        self.seat_assignments.remove(seat_assignment)

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

    def drop_courses(self, course):
        """"Removes course from the catalog"""
        self.courses.remove(course)


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
            print "Semester registered for {}".format(course_load.semester)
            for assignment in course_load.seat_assignments:
                print "Grade for Course {} is {} ".format(assignment.seat.course_offering.course.name, assignment.grade)


    def __str__(self):
        return "Student ID: {}, Student Name{}, {}".format(self.id, self.last_name,self.first_name)


if __name__ == "__main__":
    print "*************Adding university****************"
    x = University("Study Abroad University")
    print "*************Adding Colleges******************"
    print "Adding College of Engineering (COE)"
    c1 = x.add_colleges("COE")
    print "************Adding College of Business and Management Studies*********"
    c2 = x.add_colleges("Business")
    print "************Adding department Information Systems to COE*************"
    department = c1.add_department("Information Systems")

    print "**********Creating a course catalog*********************"
    course_catalog = CourseCatalog()
    print "**********Adding course DBMS to the catalog*************"
    course1 = course_catalog.add_courses("DBMS")
    print "***********Adding course web design to the catalog********"
    course2 = course_catalog.add_courses("Web Design")

    print "**************Adding the course catalog to the department Information Systems****************"
    department.add_course_catalog(course_catalog)

    print "*************Let's review the course catalog for departemnt Information System***************"
    department.view_course_catalog()

    print "***************Scheduling courses Fall 2015*********************"
    cs1 = CourseSchedule(1)

    print "*******************Assigning courses and professor to the scheduler***********"
    co1 = CourseOffering(course1,"Dr. Arnold",40)
    co2 = CourseOffering(course2,"Mr. Dave",20)

    cs1.course_offerring.append(co1)
    cs1.course_offerring.append(co2)

    print "*******************Final assignment of the schedule to the department responsible************"
    department.course_schedule_list.append(cs1)

    print "******************Printing schedule*********************"
    department.view_course_offering()

    print "*****************Adding students**********************"
    s1 = Student("Bbbbb", "Mmmmm")
    s2 = Student("Ppppp", "Ccccc")

    print "*******************Adding students to the college COE******************"
    c1.add_student(s1)
    c1.add_student(s2)

    print "***********************Printing student details*******************"
    c1.view_students()

    print "**********************Creating course load of student Bbbb for Fall 2015*****************"
    cL = s1.transcript.add_course_load(0)

    print "*******************Allocating seat for course offered DBMS*********************"
    seat = co1.assign_seat()
    seat.add_course_offering(co1)

    print "*******************Allocating seat for course offered Web Design*********************"
    seat2 = co2.assign_seat()
    seat2.add_course_offering(co2)

    print "********************Assigning the seat to student for DBMS**********************"
    seat_assignment = cL.add_seat_assignment()
    seat_assignment.add_grade("A")
    seat_assignment.assign_seat_to_student(seat)

    print "********************Assigning the seat to student for Web Design**********************"

    seat_assignment2 = cL.add_seat_assignment()
    seat_assignment2.add_grade("B")
    seat_assignment2.assign_seat_to_student(seat2)

    print "**********************View grades of student 1***********************"
    s1.view_grades_by_sem()

    print "*******Drop course DBMS*******"
    cL.drop_seat_assignment(seat_assignment)

    print "*******Reprinting grades******"
    s1.view_grades_by_sem()

    print "*****************"
    print("Viewing course offering to student 1")
    x.retrieve_college_details()




