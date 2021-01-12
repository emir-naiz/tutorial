from django.db import models

# Create your models here.
class Document(models.Model):
    marks = (
        ('private', 'private'),
        ('sergeant', 'sergeant'),
        ('lieutenant', 'lieutenant'),
        ('captain', 'captain'),
        ('major', 'major')
    )
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_unvaliable = models.DateField()
    text = models.TextField()
    mark = models.CharField(choices=marks, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'


