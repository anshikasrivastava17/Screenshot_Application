import datetime
import os
from django.conf import settings
import re

def namingfile(ss, name):
    x = datetime.datetime.now()
    y=re.sub(r'[ :-]', '', str(x)[:-7])
    img_filename = f'img{y}.png'
    img_path = os.path.join(str(settings.MEDIA_ROOT)+"/"+name, img_filename)
    ss.save(img_path)
    return img_path

def premium(name):
    if not 'premium' in name:
        return False
