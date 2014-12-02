try:
    from django.conf.urls.defaults import *

except ImportError:
    from django.conf.urls import *

urlpatterns = patterns('captcha.views',
    url(r'image/(?P<key>\w+)/$','captcha_image',name='captcha-image'),
    url(r'audio/(?P<key>\w+)/$','captcha_audio',name='captcha-audio'),
)
