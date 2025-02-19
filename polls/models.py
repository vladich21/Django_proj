import datetime

from django.db import models
from django.db import models
from django.utils import timezone

class SibTransUser(models.Model):
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text
