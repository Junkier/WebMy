from django.db import models

# Create your models here.
class Excuse(models.Model):
	content = models.TextField()
	
	def __unicode__(self):
		return self.content
		
class Emp2(models.Model):
	Empno = models.PositiveIntegerField(primary_key=True)
	Ename = models.CharField(max_length=100)
	Job   = models.TextField(blank=True) 
	Mgr   = models.PositiveIntegerField()
	HireDate = models.DateTimeField()
	Sal = models.FloatField()
	Comm = models.PositiveIntegerField(null=True)
	Deptno = models.IntegerField()
	
	def __unicode__(self):
		return self.Ename
		
		
class Emp(models.Model):
	Empno = models.PositiveIntegerField(primary_key=True)
	Ename = models.TextField(max_length=10)
	Job   = models.TextField(max_length=10)
	Sal   = models.FloatField()
	Comm  = models.IntegerField(null=True)
	
	def __unicode__(self):
		return self.Ename