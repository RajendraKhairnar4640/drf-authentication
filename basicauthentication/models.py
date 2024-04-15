from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True


tech_choices = (
    ("Python","Python"),
    ("React","React"),
    ("Devops","Devops")
)
class Employee(BaseModel):
    name = models.CharField(max_length=255)
    technology = models.CharField(max_length=255,choices=tech_choices)

    def __str__(self):
        return self.name

