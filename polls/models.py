import datetime

from django.db import models
from django.utils import timezone


class QuestionManager(models.Manager):

    def populate_polls(self):
        q = Question(question_text="What's up?", pub_date=timezone.now())
        q.save()
        q.choice_set.create(choice_text="Not much", votes=0)
        q.choice_set.create(choice_text="The sky", votes=0)
        q.choice_set.create(choice_text="Just hacking again", votes=0)

    def delete_poll(self, start_text):
        q = Question.objects.get(id=1)
        c = q.choice_set.filter(choice_text__startswith='Just hacking')
        c.delete()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    objects = QuestionManager()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text



