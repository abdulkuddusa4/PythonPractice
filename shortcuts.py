from django import template
import codecs
from django.template.engine import Engine


def get_template(template):
    try:
        with open(template,'rb') as file:

            return b''.join(file.readlines())
    except FileNotFoundError:
        print(f"file: {file} does not exists")


def get_response(request,user_list=None):
    user_list = ['roni','shafi']
    html = get_template(request)
    headers = "HTTP/1.1 200 OK\n".encode()
    headers+="content-type: text/html\n".encode()

    content = headers+html

    tmpt = template.Template(html,engine=Engine()).render(template.Context({'user_list': user_list}))
    response = codecs.decode(tmpt,'unicode_escape')
    li = list(response)
    li.pop(0),li.pop(0),li.pop()
    response = ''.join(li)
    headers+=f"content-length: {len(response)}\n\n".encode()

    return headers+response.encode()
