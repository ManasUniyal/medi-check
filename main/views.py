from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Prediction
from django.core.files.storage import FileSystemStorage
from django.conf import settings


@require_http_methods(["GET"])
def home(request):
    return render(request, 'main/homepage.html')


@require_http_methods(["POST"])
def result(request):
    upload_directory = settings.MEDIA_ROOT + str(request.user.id) + "/uploads"
    upload_file_url = None
    if request.FILES.get('image'):
        uploaded_image = request.FILES.get('image')
        fs = FileSystemStorage(location=upload_directory)  # defaults to MEDIA_ROOT
        file = fs.save(uploaded_image.name, uploaded_image)
        upload_file_url = '/images/' + str(request.user.id) + "/uploads/" + file
        print(upload_file_url)

    prediction = Prediction.objects.create(
        accuracy=95.23,
        diagnosis=Prediction.NORMAL,
        uploaded_image_url=upload_file_url
    )
    context = {
        'prediction': prediction
    }

    return render(request, 'main/result.html', context)
