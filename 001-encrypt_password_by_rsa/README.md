# 使用RSA加密传输密码

前端需要使用RSA公钥对密码进行加密，再传给后端才能正常登录。前端可以使用`jsencrypt.js`库加密。

## 启动服务

```
poetry install
poetry shell
flask run
```

## 接口调用示例数据

接口参数示例

- 帐号：`admin`
- 密码：`admin`
- 加密后的密码：`Hi62R2poR33d0bA2c3rlVxKDD8juQuS+hqC5IZ65VllAZL79mpM9+jIFdSwuFmbzTJUacrXAuHVX2Rz3YQxpaRSjavRg3XNKXMjiemE5wmV1S1cyD4zj2WZgUHAdZgKvZFN/Dc8bx6blTCmfHIrrKAj2Rs5+MN9YUsWWVnjwr1A=`

请求体

```json
{
  "username": "admin",
  "password": "Hi62R2poR33d0bA2c3rlVxKDD8juQuS+hqC5IZ65VllAZL79mpM9+jIFdSwuFmbzTJUacrXAuHVX2Rz3YQxpaRSjavRg3XNKXMjiemE5wmV1S1cyD4zj2WZgUHAdZgKvZFN/Dc8bx6blTCmfHIrrKAj2Rs5+MN9YUsWWVnjwr1A="
}
```
