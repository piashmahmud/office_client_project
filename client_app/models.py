from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Status(models.Model):
    StatusType = models.TextChoices('StatusType', 'RUNNING UPCOMING CLOSED')
    status = models.CharField(blank=False, choices=StatusType.choices, max_length=15)

    def __str__(self):
        return self.status




class Client(models.Model):
    serial_num = models.PositiveIntegerField( null=False)
    client_name = models.CharField(max_length=100,null=False)
    project_name = models.TextField(max_length=1000,null=False)
    project_details = models.TextField(blank=True, null=True)

    project_role = models.ForeignKey(Role, on_delete=models.CASCADE)

    project_status = models.ForeignKey(Status,on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %(self.client_name)


class Details(models.Model):
    serial_num = models.PositiveIntegerField( null=False)
    client_name = models.CharField(max_length=100, blank=False, null=False)
    project_name = models.CharField(max_length=100, null=False)
    team_lead = models.CharField(max_length=100, null=False)
    team_member = models.CharField(max_length=100, null=False)
    starting_date = models.DateField(blank=True, null=True)
    ending_date = models.DateField(blank=True, null=True)
    scope = models.CharField(max_length=100, blank=True, null=True)
    project_status = models.ForeignKey(Status,on_delete=models.CASCADE)
    deadline = models.CharField(max_length=100, blank=True, null=True)
    is_approved=models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" %(self.client_name, self.project_name)