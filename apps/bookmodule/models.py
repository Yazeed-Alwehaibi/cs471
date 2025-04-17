from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)


class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# lab 9
class card(models.Model):
    card_number = models.IntegerField()

    
class department(models.Model):
    name = models.CharField(max_length=100)

class course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()
    
class Student2(models.Model):
    name = models.CharField(max_length=100)
    card_number = models.OneToOneField(card, on_delete=models.PROTECT)
    department = models.ForeignKey(department, on_delete=models.CASCADE, null=True)
    course = models.ManyToManyField(course)
