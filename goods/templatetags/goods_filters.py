from django.template import Library

register = Library()


# 构建图片
def create_image(index):
    image = 'images/banner0' + str(index) + '.jpg'
    return image

register.filter('create_image', create_image)


