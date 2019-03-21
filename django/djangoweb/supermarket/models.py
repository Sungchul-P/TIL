from django.db import models

class Play(models.Model):
    original = models.CharField(max_length=30)
    encrypted = models.CharField(max_length=200)
    decrypted = models.CharField(max_length=30)

    # class Meta:
    #     managed = False
    #     db_table = 'play'

class Supermarket(models.Model):
    itemno = models.IntegerField(db_column='Itemno')
    category = models.CharField(db_column='Category', max_length=20)
    foodname = models.CharField(db_column='FoodName', max_length=30)
    company = models.CharField(db_column='Company', max_length=20)
    price = models.IntegerField(db_column='Price')

    # class Meta:
    #     managed = False
    #     db_table = 'supermarket'