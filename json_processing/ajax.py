import json
from datetime import datetime
from django.http import JsonResponse

from .forms import UploadFileForm
from .models import Record


def upload_file(request):
    """Загрузка json файла"""

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            return JsonResponse(handle_uploaded_file(request.FILES['file']))
    return JsonResponse({'status': 'error'})


def handle_uploaded_file(file):
    """Обработка файла и сохранение данных"""

    try:
        file_content = file.read()
        json_data = json.loads(file_content)
        for record in json_data:
            name = record.get('name', None)
            date = record.get('date', None)
            if name is None:
                return {'status': 'error', 'message': 'Не передан ключ name.'}
            if date is None:
                return {'status': 'error', 'message': 'Не передан ключ date.'}
            if len(name) >= 50:
                return {
                    'status': 'error',
                    'message': 'Длина значения name должна быть меньше 50 символов.'
                }
            try:
                date = datetime.strptime(date, '%Y-%m-%d_%H:%M')
            except ValueError:
                return {
                    'status': 'error',
                    'message': 'Неправильный формат поля date. Требуемый формат: YYYY-MM-DD_HH:mm.'
                }
            Record.objects.create(name=name, date=date)
        return {'status': 'ok'}
    except Exception:
        return {'status': 'error', 'message': 'Неизвестная ошибка.'}
