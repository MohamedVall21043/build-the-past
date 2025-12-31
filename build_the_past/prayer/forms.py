from django import forms
from .models import QadaaSalat , Prayer

class QadaaForm(forms.ModelForm):
    class Meta:
        model = QadaaSalat
        fields = ['start_date', 'repentance_date', 'daily_qadaa']




from .models import QadaaSession

class QadaaSessionForm(forms.ModelForm):
    class Meta:
        model = QadaaSession
        fields = ['start_date', 'repentance_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'repentance_date': forms.DateInput(attrs={'type': 'date'}),
        }


class PrayerUpdateForm(forms.ModelForm):
    class Meta:
        model = Prayer
        fields = ['done', 'note']
        widgets = {
            'note': forms.TextInput(attrs={'placeholder': 'أدخل ملاحظتك هنا'}),
        }