# 如果访问 http://localhost:8080/?person=Jim，响应会变成字符串 'Hello Jim!'

# $ curl -i http://localhost:8080/?person=Jim
# HTTP/1.0 200 OK
# Date: Tue, 31 Mar 2020 08:46:21 GMT
# Server: WSGIServer/0.2 CPython/3.8.2
# Content-Type: text/html; charset=UTF-8
# Content-Length: 10
#
# Hello Jim!
