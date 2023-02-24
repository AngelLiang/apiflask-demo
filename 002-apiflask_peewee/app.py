import datetime
import json
from peewee import CharField,ForeignKeyField,TextField,DateTimeField
from playhouse.shortcuts import model_to_dict

from apiflask import APIFlask
from apiflask import Schema, fields


from playhouse.flask_utils import FlaskDB as _FlaskDB
from pagination import PaginatedQuery

class FlaskDB(_FlaskDB):

    def connect_db(self):
        from flask import request
        if self._excluded_routes and request.endpoint in self._excluded_routes:
            return
        if not self.database.is_closed():
            return
        self.database.connect()


SECRET_KEY = 'secret-key'
# DATABASE = 'sqlite:///db.sqlite3'
DATABASE = 'mysql://root:Bingo@123@192.168.42.8:3306/apiflask'

# If we want to exclude particular views from the automatic connection
# management, we list them this way:
# FLASKDB_EXCLUDED_ROUTES = ('logout',)

app = APIFlask(__name__, title='接口文档', version='1.0')
app.config.from_object(__name__)


class BaseResponse(Schema):
    code = fields.Integer(load_default=0)
    msg = fields.String(load_default='操作成功！')
    data = fields.Field()  # the data key


app.config['BASE_RESPONSE_SCHEMA'] = BaseResponse

db_wrapper = FlaskDB(app)


class BaseModel(db_wrapper.Model):

    def to_dict(self):
        return model_to_dict(self, backrefs=True)

    def to_json(self):
        data = self.to_dict()
        return json.dumps(data, default=str)


class User(BaseModel):
    username = CharField(unique=True)

    class Meta:
        table_name = 'user'


class Tweet(BaseModel):
    user = ForeignKeyField(User, backref='tweets')
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        table_name = 'tweet'


class UserOut(Schema):
    id = fields.Integer()
    username = fields.String()


class UserListOut(Schema):
    records = fields.List(fields.Nested(UserOut))
    total = fields.Integer()


@app.get('/api/v1/user')
@app.output(UserListOut)
def get_user_list():
    paginated_query = PaginatedQuery(User)
    object_list = paginated_query.get_object_list()
    total = paginated_query.get_object_total()
    return {
        'code': 0,
        'data': {
            'total': total,
            'records': object_list
        }
    }


@app.get('/api/v1/user/<int:id>')
@app.output(UserOut)
def get_user(id):
    instance = User.select().where(User.id==id).first()
    if instance:
        print(instance.to_dict())
        if instance:
            return {
                'code': 0,
                'data': instance.to_dict()
            }
    return {
        'code': 1
    }



class TweetOut(Schema):
    id = fields.Integer()
    content = fields.String()
    timestamp = fields.DateTime()


class TweetListOut(Schema):
    records = fields.List(fields.Nested(TweetOut))
    total = fields.Integer()


@app.get('/api/v1/tweet')
@app.output(TweetListOut)
def get_tweet_list():
    paginated_query = PaginatedQuery(Tweet)
    object_list = paginated_query.get_object_list()
    total = paginated_query.get_object_total()
    return {
        'code': 0,
        'data': {
            'total': total,
            'records': object_list
        }
    }

@app.get('/api/v1/tweet/<int:id>')
@app.output(TweetOut)
def get_tweet(id):
    instance = Tweet.select().where(Tweet.id==id).first()
    if instance:
        print(instance.to_json())
        if instance:
            return {
                'code': 0,
                'data': instance.to_dict()
            }
    return {
        'code': 1
    }


if __name__ == "__main__":
    app.run()
