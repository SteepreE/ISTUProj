from redis import Redis
from ScheduleParser.scheduleParser import ScheduleParser
from .singleton import singleton


@singleton
class LessonsDB:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def _connect(self) -> Redis:
        return Redis(host=self.host, port=self.port, decode_responses=True)

    def update_lessons(self) -> None:
        db = self._connect()

        groups_schedule = ScheduleParser.get_schedule()
        db.mset(groups_schedule)

        db.close()

    def get_lesson(self, group: str) -> dict:
        db = self._connect()

        lesson, cabinet = str(db.get(group)).split('|')
        db.close()

        return {"lesson": lesson, "cabinet": cabinet}
