from os import name
from api.models import Branch, College, Textbook
import random
import json
import datetime

def populate_users(UserClass, jsonFilePath):
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)

    for item in dict_data:
        user = UserClass(**item)
        user.save()

def populate_subjects(SubjectClass, jsonFilePath):
    """./util/subjects_data.json"""
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)

    for item in dict_data:
        try:
            str(item['subject_code'])
        except KeyError:
            item['subject_code'] = item['code']
            del item['code']

        user = SubjectClass(**item)
        user.save()

def populate_courses(CourseClass, jsonFilePath):
    """./util/courses_data.json"""
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)

    for item in dict_data:
        user = CourseClass(**item)
        user.save()

def populate_branch(BranchClass, jsonFilePath):
    """./util/branches_data.json"""
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)

    for item in dict_data:
        user = BranchClass(**item)
        user.save()

def list_objects(modelClass):
    for item in modelClass.objects.all():
        print(item)


def populate_textbooks(TextbookClass, branches, courses, subjects, users, jsonFilePath):
    """./util/textbooks_data.json"""
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)
    YEARS = [
        'FIRST',
        'SECOND',
        'THIRD',
        'FOURTH',
    ]

    for book in dict_data:
        textbook = TextbookClass(
            title = book['title'],
            # author = book['author'],
            link ="https://drive.google.com/file/d/1MewBpDc6Y5_9-ZluGARQG04T75xhVjzV/view",
            # cover_image = book['cover_image'],
            subject = random.choice(subjects.objects.all()),
            branch = random.choice(branches.objects.all()),
            course = random.choice(courses.objects.all()),
            year= random.choice(YEARS),
            posted_by = random.choice(users.objects.all()),
            description = book['description'],
        )
        textbook.save()


def populate_lectures(LectureClass, SubjectClass, jsonFilePath):
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)

    for lec in dict_data:
        lecture = LectureClass(
            subject=SubjectClass.objects.get(subject_code=lec['subject']),
            start_time=datetime.datetime.strptime(lec['start_time'], '%H:%M:%S').time(),
            end_time=datetime.datetime.strptime(lec['end_time'], '%H:%M:%S').time(),
            teacher=lec['teacher']
        )
        lecture.save()


def populate_faculty(FacultyClass, BranchClass, CollegeClass, jsonFilePath):
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)

    for person in dict_data:
        prof = FacultyClass(
            name = person['name'],
            college = CollegeClass.objects.get(college_code='NITG'),
            designation = person['designation'],
            email = person['email'],
            description = person['description'],
            branch = BranchClass.objects.get(branch_code=person['branch_code'])
        )
        prof.save()

def populate_colleges(CollegeClass, jsonFilePath):
    json_data = open(jsonFilePath, 'r')
    dict_data = json.load(json_data)


    for college in dict_data:
        description = f"""Institute Name : {college['full_name']}
Address : {college['full_address']}
Institute Type : {college['institute_type']}
Established : {college['established']}"""
        
        col = CollegeClass(
            college_code = college['college_code'],
            name = college['short_name'],
            description = description,
            location = college['location'],
            college_image = college['college_image'],
            link_image = college['college_logo_img']
        )
        col.save()

def populate_portion_list_for_nitgoa(Portion, Subject, College):
    for sub in Subject.objects.all():
        portion = Portion(
            subject=sub,
            college=College.objects.get(college_code='NITG'),
            link="https://drive.google.com/file/d/1MewBpDc6Y5_9-ZluGARQG04T75xhVjzV/view"
        )
        portion.save()