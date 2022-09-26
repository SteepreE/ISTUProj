import json

from flask import Flask

from Database.lessonsDB import LessonsDB
from Database.studentsDB import StudentsDB

from datetime import datetime

from DataReiciver import receive_data

app = Flask(__name__)

APP_HOST = "localhost"
APP_PORT = 8080

STUDENT_DB_PASS = "steeptowin"
STUDENT_DB_URL = f"mongodb+srv://steepree:{STUDENT_DB_PASS}@cluster0.bs0aqq7.mongodb.net/?retryWrites=true&w=majority"

LESSONS_DB_HOST = "localhost"
LESSONS_DB_PORT = 6379

students_DB = StudentsDB(STUDENT_DB_URL)
lessons_DB = LessonsDB(LESSONS_DB_HOST, LESSONS_DB_PORT)


@app.route("/post_user_visit", methods=['POST'])
def post_data(request):
    try:
        data = request.json

        student_id = data["id"]
        group = data["group"]
        cabinet = data["cabinet"]

        current_lesson = lessons_DB.get_lesson(group)

        if cabinet != current_lesson["cabinet"]:
            return {"success": False}

        students_DB.add_visit(student_id, current_lesson["lesson"], datetime.now())
        return {"success": True}
    except:
        return {"success": False}


@app.route("/get_all_visits", methods=['GET'])
def get_data(request):
    try:
        visits = json.dumps(students_DB.get_all_students())
        return visits
    except:
        return {"success": False}


if __name__ == '__main__':
    receive_data()

#    app.run(host=APP_HOST, port=APP_PORT)
