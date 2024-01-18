from datetime import datetime
from django.db import models

# Create your models here.
class posts(models.Model):
    tweet_id=models.AutoField
    author_name =models.CharField(max_length=40)
    content=models.CharField(max_length=300)
    pub_date =models.DateField(auto_now_add=True)
    pub_time = models.TimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        # Set pub_time to the current time if pub_date is not provided
        if not self.pub_date:
            self.pub_date = datetime.now()
        self.pub_time = self.pub_date.time()
        super().save(*args, **kwargs)