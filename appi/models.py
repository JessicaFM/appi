from django.db import models

class AppiRequest(models.Model):
    type = models.CharField(max_length=10)
    url = models.CharField(max_length=200)
    header = models.TextField()
    body = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def list(self):
        "Return a list of all requests."
        return AppiRequest.objects.all()