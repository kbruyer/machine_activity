from django.db import models


class DailyActivityPost(models.Model):
    description = models.TextField(max_length=500, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description
