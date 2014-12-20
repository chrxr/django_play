import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):            
        return self.question_text
    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.choice_text

class Client(models.Model):
    client_name = models.CharField(max_length=200)

    @classmethod
    def create(cls, client_name):
        client = cls(client_name=client_name)
        # do something with the book
        return client

    def __unicode__(self):              # __unicode__ on Python 2
	    return self.client_name


class RateCard(models.Model):
	rate_card_name = models.CharField(max_length=200)
	client = models.ForeignKey(Client)

	def __unicode__(self):              # __unicode__ on Python 2
	    return self.rate_card_name

class Project(models.Model):
	project_name = models.CharField(max_length=200)
	client = models.ForeignKey(Client)
	rate_card = models.ForeignKey(RateCard)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.project_name

class Task(models.Model):
	task_name = models.CharField(max_length=200)
	time_days = models.FloatField()
	time_hours = models.FloatField()
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	project = models.ForeignKey(Project)

	def __unicode__(self):              # __unicode__ on Python 2
	    return self.task_name

class Rate(models.Model):
	rate_name = models.CharField(max_length=200)
	rate_per_hour = models.FloatField()
	rate_per_day = models.FloatField()
	rate_card = models.ForeignKey(RateCard)

	def __unicode__(self):              # __unicode__ on Python 2
	    return self.rate_name
