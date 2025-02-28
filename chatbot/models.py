from django.db import models


class Documentation(models.Model):
    cdp = models.CharField(max_length=50)
    url = models.URLField()
    content = models.TextField()

    class Meta:
        unique_together = ('cdp', 'url')  # Prevent duplicates

    def __str__(self):
        return f"{self.cdp} - {self.url}"