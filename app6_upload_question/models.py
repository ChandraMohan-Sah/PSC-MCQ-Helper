from django.db import models
from django.contrib.auth.models import User
from datetime import date

class MCQ(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


class ExamAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')
    score = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.exam_date} - {self.status}"

    def mark_completed(self, score):
        self.status = 'Completed'
        self.score = score
        self.save()

    @classmethod
    def get_exam_status(cls, user, exam_date):
        return cls.objects.filter(user=user, exam_date=exam_date).first()