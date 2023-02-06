from peewee import CharField
from playhouse.flask_utils import FlaskDB, PaginatedQuery

from apiflask import APIFlask
from apiflask import Schema, fields

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


class UserOut(Schema):
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
        'code': 1,
        'data': {
            'records': object_list
        }
    }


if __name__ == "__main__":
    app.run()
