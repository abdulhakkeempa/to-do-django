import os
from django.core.management.utils import get_random_secret_key  

with open('.env', 'w') as fp:
    #generate secret key automatically
    key = get_random_secret_key()
    fp.write('SECRET_KEY="'+key+'"')
    fp.close()