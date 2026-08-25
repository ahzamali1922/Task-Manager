from django.db import models
# connecting user and tasks table
from django.conf import settings
# Create your models here.

# task table
class Task(models.Model):
    title = models.CharField(max_length= 50)
    description = models.TextField(blank = True)
    completed = models.BooleanField(default = False)
    PRIORITY_CHOICES = [
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH'),
        ('extremely_high', 'EXTREMELY_HIGH'),
    ]
    priority = models.CharField(max_length= 20, choices= PRIORITY_CHOICES, default= 'medium')
    due_date = models.DateTimeField(null = True, blank = True)
    created_date = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    CATEGORY_CHOICES = [
        ('personal', 'PERSONAL'),
        ('work','WORK'),
        ('study','STUDY'),
        ('shopping','SHOPPING'),
        ('programming','PROGRAMMING'),
        ('sports','SPORTS'),
        ('gaming','GAMING'),
        ('others','OTHERS'),
    ]
    category = models.CharField(max_length= 20, choices= CATEGORY_CHOICES, default= 'others')
    # foreign key users -- task
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE,
        null = True,
        blank = True,
    )

    def __str__(self):
        return self.title

#Category 
class Category(models.Model):
    name = models.CharField(max_length= 30)
    description = models.TextField(blank = True)

    def __str__(self):
        return self.name

