import datetime
from peewee import CharField,ForeignKeyField,TextField,DateTimeField
from playhouse.flask_utils import PaginatedQuery
from playhouse.shortcuts import model_to_dict

from apiflask import APIFlask
from apiflask import Schema, fields


from playhouse.flask_utils import FlaskDB as _FlaskDB


class FlaskDB(_FlaskDB):

    def connect_db(self):
        from flask import request
        if self._excluded_routes and request.endpoint in self._excluded_routes:
            return
        if not self.database.is_closed():
            return
        self.database.connect()


SECRET_KEY = 'secret-key'
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


class User(db_wrapper.Model):
    username = CharField(unique=True)

    class Meta:
        table_name = 'user'

    def to_dict(self):
        return model_to_dict(self, backrefs=True)


class Tweet(db_wrapper.Model):
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


@app.get('/api/v1/user')
@app.output(UserListOut)
def get_user_list():
    # query = User.select()
    paginated_query = PaginatedQuery(User, 10,)
    count = paginated_query.get_page_count()
    object_list = paginated_query.get_object_list()
    print((count, object_list))
    return {
        'code': 0,
        'data': {
            'records': object_list
        }
    }


@app.get('/api/v1/user/<int:id>')
@app.output(UserOut)
def get_user(id):
    instance = User.select().where(User.id==id).first()
    print(instance.to_dict())
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
