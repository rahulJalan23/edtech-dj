from api.models import Textbook
import random
import json

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
            author = book['author'],
            link = book['link'],
            cover_image = book['cover_image'],
            subject = random.choice(subjects.objects.all()),
            branch = random.choice(branches.objects.all()),
            course = random.choice(courses.objects.all()),
            year= random.choice(YEARS),
            posted_by = random.choice(users.objects.all()),
            description = book['description'],
        )
        textbook.save()