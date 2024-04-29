from django.db import models
from django.contrib import admin

class Temperature(models.Model):
    temperature = models.FloatField()
    smiley = models.BooleanField(default=False)
    date_recorded = models.DateTimeField(auto_now=True)
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.date_recorded, self.smiley, self.temperature, self.remarks) 
    
    def datecreated(self):
        return self.date_recorded.strftime('%B %d %Y')
    
class TemperatureAdmin(admin.ModelAdmin):
    list_display = ['date_recorded', 'temperature', 'smiley', 'remarks',]

