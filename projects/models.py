from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    has_tests = models.BooleanField()
    has_docs = models.BooleanField()

    class Status(models.TextChoices):
        NA = "NA", "na"
        PLANNED = "PL", "Planned"
        STARTED = "ST", "Started"
        FIRST_RESULTS = "FR", "First results"
        MATURE_RESULTS = "MR", "Mature results"
        DONE = "DO", "Done"
        DEFERRED = "DE", "Deferred"
        BLOCKED = "BL", "Blocked"
        INACTIVE = "IN", "Inactive"

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.NA)

    last_review = models.DateField(null=True, blank=True)

    def is_at_risk(self):
        return self.status in {self.Status.BLOCKED, self.Status.INACTIVE}

    def __str__(self):
        return self.name



