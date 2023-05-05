from apiflask import APIFlask, Schema
from apiflask.fields import File
from flask import send_from_directory, send_file
import json
from io import BytesIO

SECRET_KEY='secret-key'


app = APIFlask(__name__, title='接口文档', version='1.0')
app.config.from_object(__name__)


@app.get('/downloadFile')
def download_file():
    export_data = [{'hello': 'world'}]
    f = BytesIO()
    data = json.dumps(export_data, ensure_ascii=False, default=str)
    f.write(data.encode())
    f.seek(0)
    return send_file(f, as_attachment=True, download_name='file.json')


if __name__ == "__main__":
    app.run()
