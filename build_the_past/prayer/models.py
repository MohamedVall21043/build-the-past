from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta, date

class QadaaSalat(models.Model):
    start_date = models.DateField(help_text="تاريخ بداية ترك الصلاة")
    repentance_date = models.DateField(help_text="تاريخ التوبة")
    daily_qadaa = models.PositiveIntegerField(help_text="عدد الصلوات المقضية يوميًا")
    completed_prayers = models.PositiveIntegerField(default=0)

    def total_missed_prayers(self):
        days = (self.repentance_date - self.start_date).days
        return days * 5

    def remaining_prayers(self):
        return self.total_missed_prayers() - self.completed_prayers











































































class Prayer(models.Model):
    PRAYER_CHOICES = [
        ('Fajr', 'الفجر'),
        ('Dhuhr', 'الظهر'),
        ('Asr', 'العصر'),
        ('Maghrib', 'المغرب'),
        ('Isha', 'العشاء'),
    ]

    prayer_date = models.DateField()
    prayer_name = models.CharField(max_length=10, choices=PRAYER_CHOICES)
    done = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.prayer_name} - {self.prayer_date}"

class QadaaSession(models.Model):
    start_date = models.DateField(help_text="تاريخ بداية ترك الصلاة")
    repentance_date = models.DateField(help_text="تاريخ التوبة")

    def create_prayers(self):
        """إضافة جميع الصلوات الفائتة بين start_date و repentance_date"""
        current = self.start_date
        prayers = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

        while current <= self.repentance_date:
            for p in prayers:
                Prayer.objects.create(prayer_date=current, prayer_name=p)
            current += timedelta(days=1)

    def __str__(self):
        return f"جلسة قضاء من {self.start_date} إلى {self.repentance_date}"