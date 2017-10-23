from django.db import models
from django.utils import timezone

class Post(models.Model):
    KEK = 'keking'
    LOL = 'loling'
    HEH = 'hehing'
    LMAO = 'lmaoing'
    OR_CHOICES = (
        (KEK,'kek'),
        (LOL,'lol'),
        (HEH,'heh'),
        (LMAO,'lmao'),
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default = 'Title')
    text = models.TextField(default = 'Text')
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)
    question = models.CharField(max_length=15, choices=OR_CHOICES,default=LOL)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
