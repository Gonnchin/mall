from utils.wrappers import *


# 判断用户是否登陆
def user_is_login(request):
    return get_session(request, 'user_name') and get_session(request, 'uid')
