import pymongo

from datetime import datetime
from .singleton import singleton


@singleton
class StudentsDB:
    def __init__(self, connect_url):
        self.connect_url = connect_url

    def _connect(self) -> pymongo.MongoClient:
        return pymongo.MongoClient(self.connect_url)

    def get_all_students(self):
        pass

    def add_visit(self, student_id: str, lesson: str, d_time: datetime):
        connection = self._connect()
        db = connection.get_database("main")
        collection = db.get_collection("students")

        collection.update_one(
            {"_id": student_id},
            {"$push": {
                "visits": {
                    "lesson": lesson,
                    "datetime": d_time
                }
            }
            }
        )

    def add_student(self, student_id: str, fullname: str, group: str):
        connection = self._connect()
        db = connection.get_database("main")
        collection = db.get_collection("students")

        collection.insert_one({
            "_id": student_id,
            "fullname": fullname,
            "group": group,
            "visits": []
        })

        connection.close()
