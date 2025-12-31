from django.shortcuts import render, redirect
from .forms import QadaaSessionForm , PrayerUpdateForm
from .models import QadaaSession, Prayer
from django.shortcuts import get_object_or_404
from datetime import date


def setup_qadaa(request):
    if request.method == 'POST':
        form = QadaaSessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            session.create_prayers()  # هنا يتم إنشاء كل الصلوات تلقائيًا
            return redirect('prayers_list')
    else:
        form = QadaaSessionForm()
    return render(request, 'setup.html', {'form': form})

def prayers_list(request):
    end_date = date(2014, 12, 31)
    prayers = Prayer.objects.filter(prayer_date__lte=end_date).order_by('prayer_date')

    if request.method == 'POST':
        prayer_id = request.POST.get('prayer_id')
        prayer = get_object_or_404(Prayer, id=prayer_id)
        form = PrayerUpdateForm(request.POST, instance=prayer)
        if form.is_valid():
            form.save()
            return redirect('prayers_list')

    return render(request, 'prayers_list.html', {'prayers': prayers})
