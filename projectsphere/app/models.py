from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class StudentReg(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=128)
	teamHeadName = models.CharField(max_length=128)
	teamHeadId = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	

class Co_ordinatorReg(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=128)
	

class GuideReg(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=128)
	

class RegisterProject(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	student = models.ForeignKey(StudentReg, on_delete=models.CASCADE)
	teamName = models.CharField(max_length=128)
	projectTitle = models.CharField(max_length=128)
	teamHeadName = models.CharField(max_length=128)
	teamHeadId = models.CharField(max_length=128)
	username = models.CharField(max_length=128)
	teamMember1 = models.CharField(max_length=128)
	teamMember2 = models.CharField(max_length=128)
	teamMember3 = models.CharField(max_length=128)
	teamMember1Id = models.CharField(max_length=128)
	teamMember2Id = models.CharField(max_length=128)
	teamMember3Id = models.CharField(max_length=128)
	assign = models.CharField(max_length=128,null=True)
	guide = models.ForeignKey(GuideReg, on_delete=models.CASCADE,null=True)
	

class ProjectAnnouncement(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	co_ordinator = models.ForeignKey(Co_ordinatorReg, on_delete=models.CASCADE)
	subject = models.CharField(max_length=128)
	message = models.CharField(max_length=128)
	now_date = models.DateField(max_length=128,null=True)
	date = models.DateField(max_length=128,null=True)

class Chat(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=128)
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	
	
class Calender(models.Model):
	week = models.CharField(max_length=128)
	submit = models.CharField(max_length=128)
	
class Resource(models.Model):
	calender = models.ForeignKey(Calender, on_delete=models.CASCADE)
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	drive_link = models.CharField(max_length=1000)

class ReviewOne(models.Model):
	ident_pro=models.IntegerField()
	liter_review=models.IntegerField()
	obj_des_meth=models.IntegerField()
	total=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)

class ReviewTwo(models.Model):
	det_meth_algo=models.IntegerField()
	pro_implement=models.IntegerField()
	viva=models.IntegerField()
	total=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)

class ReviewThree(models.Model):
	level_com_demo=models.IntegerField()
	total=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)

class GuideMark(models.Model):
	reg_std_mini_pro=models.IntegerField()
	know_invol_work=models.IntegerField()
	total=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)

class EndSemEval(models.Model):
	ppt=models.IntegerField()
	presentation=models.IntegerField()
	demo=models.IntegerField()
	viva=models.IntegerField()
	total=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)


class AttendenceTab(models.Model):
	attendence=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)

class ReportTab(models.Model):
	report=models.IntegerField()
	project = models.ForeignKey(RegisterProject, on_delete=models.CASCADE)
	projectTitle = models.CharField(max_length=128)
	Name = models.CharField(max_length=128)
	memberId = models.CharField(max_length=128)