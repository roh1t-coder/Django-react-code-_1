from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    region = models.CharField(max_length=100)

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='ideas')

class Vote(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='votes')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=10)

class Collaboration(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='collaborations')
    employees = models.ManyToManyField(Employee)
    status = models.CharField(max_length=50)

class Reward(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='rewards')
    reward_type = models.CharField(max_length=100)
    status = models.CharField(max_length=50)