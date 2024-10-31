from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    created_date = models.DateTimeField("publish date",auto_now=True)
    def __str__(self):
        return self.question_text

class Question_choice(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE,blank=True)
    choice_text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

