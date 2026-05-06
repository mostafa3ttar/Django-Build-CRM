from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
import uuid
from django.utils.text import slugify
from django.core.validators import RegexValidator


# Create your models here.


# category model
class Category (models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
# client model
phone_regex = RegexValidator(
    regex=r'^\d{9,15}$', 
    message="Phone number must be 9-15 digits and contain only numbers."
)
class Record(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(validators=[phone_regex], max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tall = models.IntegerField()
    weight = models.IntegerField()
    address = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)
    
    slug = models.SlugField(null=True, blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        if not self.slug:
            original_slug = slugify(self.first_name +" "+ self.last_name)    ##logic
            self.slug = f"{original_slug}-{str(uuid.uuid4())[:4]}"
        super(Record,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    
    class Meta:
        ordering = ['-id']