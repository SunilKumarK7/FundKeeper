from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=200)
    amount=models.IntegerField()
    
    expense_categories=(
        ("Housing","Housing"),
        ("Transportation","Transportation"),
        ("Food","Food"),
        ("Health","Health"),
        ("Entertainment","Entertainment"),
        ("DebtPayments","Debt Payments"),
        ("PersonalCare","Personal Care"),
        ("Education","Education"),
        ("Savings","Savings"),
        ("Miscellaneous","Miscellaneous"),
    )
    category=models.CharField(max_length=200,choices=expense_categories,default="Miscellaneous")
    user_object=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    
    priority_options=(
        ("need","need"),
        ("want","want")    
    )
    priority=models.CharField(max_length=200,choices=priority_options,default="need")
    
    def __str__(self):
        return self.title
    

class Income(models.Model):
    title=models.CharField(max_length=200)
    amount=models.IntegerField()
    
    income_categories = (
        ("Salary","Salary"),
        ("Business","Business"),
        ("Investment","Investment"),
        ("Rental","Rental"),
        ("Interest","Interest"),
        ("Dividend","Dividend"),
        ("Royalty","Royalty"),
        ("Capital","Capital"),
        ("Pension","Pension"),
        ("SocialSecurity","SocialSecurity"),
    )
    category=models.CharField(max_length=200,choices=income_categories,default="Salary")
    
    user_object=models.ForeignKey(User,models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title