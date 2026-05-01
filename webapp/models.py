from django.db import models
import uuid
from django.utils.text import slugify


# Create your models here.


# category model
class Category (models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
# client model
class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tall = models.IntegerField()
    weight = models.IntegerField()
    address = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.first_name +" "+ self.last_name)    ##logic
            self.slug = f"{original_slug}-{str(uuid.uuid4())[:4]}"
        super(Record,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    
    class Meta:
        ordering = ['-id']