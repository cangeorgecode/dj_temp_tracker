from django.db import models
from django.contrib import admin

class Temperature(models.Model):
    temperature = models.FloatField()
    date_recorded = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.date_recorded, self.temperature) 
    
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['date_recorded', 'temperature']

