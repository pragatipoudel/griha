from django.db import models


class Process(models.Model):
    def __str__(self):
        return 'Process'


class ProcessStep(models.Model):
    process = models.ForeignKey(Process, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['step_number']

