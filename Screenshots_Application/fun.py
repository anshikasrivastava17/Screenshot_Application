import datetime
import os
from django.conf import settings
import re

def namingfile(ss):
    x = datetime.datetime.now()
    y=re.sub(r'[ :-]', '', str(x)[:-7])
    img_filename = f'myimg{y}.png'
    img_path = os.path.join(settings.MEDIA_ROOT, img_filename)
    ss.save(img_path)
    return img_path