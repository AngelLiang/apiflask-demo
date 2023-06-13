import json
from playhouse.flask_utils import FlaskDB as _FlaskDB
from playhouse.shortcuts import model_to_dict
from flask import request


class FlaskDB(_FlaskDB):

    def connect_db(self):
        if self._excluded_routes and request.endpoint in self._excluded_routes:
            return
        if not self.database.is_closed():
            return
        self.database.connect()


db_wrapper = FlaskDB()


class BaseModel(db_wrapper.Model):

    def __str__(self) -> str:
        return f'<{self.__class__.__name__} {self.get_id()}>'

    def to_dict(self):
        return model_to_dict(self)

    def to_json(self):
        data = self.to_dict()
        return json.dumps(data, default=str)
