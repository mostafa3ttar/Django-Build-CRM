from django.db import models

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
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    
    class Meta:
        ordering = ['-id']