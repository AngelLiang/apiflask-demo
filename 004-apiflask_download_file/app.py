from apiflask import APIFlask, Schema
from apiflask.fields import File
from flask import send_from_directory, send_file
import json
from io import BytesIO

SECRET_KEY='secret-key'


app = APIFlask(__name__, title='接口文档', version='1.0')
app.config.from_object(__name__)


@app.get('/downloadJson')
def download_json():
    export_data = [{'hello': 'world'}]
    f = BytesIO()
    data = json.dumps(export_data, ensure_ascii=False, default=str)
    f.write(data.encode())
    f.seek(0)
    return send_file(f, as_attachment=True, download_name='file.json')


class Area:
    def __init__(self,id,name) -> None:
        self.id=0
        self.name=''

    def __str__(self) -> str:
        return self.name

class User:

    def __init__(self,id,name,phone,area) -> None:
        self.id=id
        self.name=name
        self.phone=phone
        self.area=area


def export_excel(records):
    import xlwt
    from io import BytesIO

    wb = xlwt.Workbook()
    sheet = wb.add_sheet('sheet1')
    colnames = ('ID', '姓名', '手机号码', '区域')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)
    props = ('id', 'name', 'phone', 'area')
    for row, instance in enumerate(records):
        for col, prop in enumerate(props):
            if prop == 'area':
                value = instance.area
                if isinstance(value, Area) and value:
                    value = str(value)
                sheet.write(row + 1, col, value)
                continue

            value = getattr(instance, prop, '')
            sheet.write(row + 1, col, value)

    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer

@app.get('/downloadExcel')
def download_excel():
    area = Area(1,'area')
    records = [
        User(1,'user01','158', area),
        User(2,'user02','158', area),
        User(3,'user03','158', area)
    ]
    filedata = export_excel(records)
    return send_file(filedata, as_attachment=True, download_name='file.xls')


if __name__ == "__main__":
    app.run()
