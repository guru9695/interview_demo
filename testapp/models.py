from django.db import models
from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4

    
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    ext1 = filename.split('.')[0]
    print('%%%%%%%%%55',ext1)
    data=Item.objects.all().last()
    print('$$$$$$$$$$$$$$$',data.image,data.id,ext)    
    filename = "%s.0000%s.%s" %(ext1,data.id,ext)
    return os.path.join(instance.directory_string_var, filename)
  
class Item(models.Model):
    # slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to = get_file_path)
       
    directory_string_var = 'DDDS_0000001'
    
    Created_By = models.IntegerField(blank=True, null=True)