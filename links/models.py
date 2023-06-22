from django.db import models
from users.models import Users


class Links(models.Model):
    id = models.BigAutoField(primary_key=True)
    link = models.TextField(null=False, blank=False)
    link_to = models.TextField(null=False, blank=False)
    user_id = models.ForeignKey(to=Users, on_delete=models.CASCADE, null=False)
    created_time = models.DateTimeField(auto_now=True)
    visited_times = models.BigIntegerField(default=0)
    class Meta:
        pass
