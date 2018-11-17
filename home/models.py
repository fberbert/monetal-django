from django.db import models

class OnePage(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    menu_name = models.CharField(max_length=50,null=False,blank=False)
    show_menu = models.BooleanField(default=True)
    order = models.IntegerField(null=False)
    active = models.BooleanField(default=False)
    content = models.TextField()



