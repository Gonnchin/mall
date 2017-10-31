import hashlib
from django.contrib import messages


def post(request, key):
    return request.POST.get(key, '').strip()


def get(request, key):
    return request.GET.get(key, '').strip()


def post_list(request, key):
    return request.POST.getlist(key, '')


# 密码加密函数
def password_encryption(password, salt=''):
    # salt=''为可传字符串,和密码拼接在一起在次加密
    sha = hashlib.sha256()
    new_password = '@#$4' + password + '@#%$'
    sha.update(new_password.encode('utf-8'))
    return sha.hexdigest()


# 添加消息
def add_message(request, key, value):
    messages.add_message(request, messages.INFO, key+':'+value)


# 获取消息
def get_messages(request):
    info = messages.get_messages(request)
    info_dic = dict()
    for mess in info:
        # 获取的消息是对象,转换成字符串类型
        content = str(mess).split(':')
        info_dic[content[0]] = content[1]
    return info_dic


# 设置cookie
def set_cookie(response, key, value):
    response.set_cookie(key, value, max_age=60*60*12)


# 获取cookie
def get_cookie(request, key):
    request.cookie.get(key, '')


# 删除cookie
def del_cookie(response, key):
    response.delete_cookie(key)


# 设置session
def set_session(request, key, value):
    request.session[key] = value


# 获取session
def get_session(request, key):
    return request.session.get(key, '')


# 删除session
def del_session(request):
    request.session.flush()










