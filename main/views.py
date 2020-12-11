from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Prediction
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from cnn_model import compute_result


@require_http_methods(["GET"])
def home(request):
    return render(request, 'main/homepage.html')


@require_http_methods(["POST"])
def result(request):
    upload_directory = settings.MEDIA_ROOT + str(request.user.id) + "/uploads/"
    result_directory = settings.MEDIA_ROOT + str(request.user.id) + "/results/"
    upload_file_url = None
    processed_file_url = None
    diagnosis = Prediction.NORMAL

    if request.FILES.get('image'):
        uploaded_image = request.FILES.get('image')
        fs = FileSystemStorage(location=upload_directory)  # defaults to MEDIA_ROOT
        file_name = fs.save(uploaded_image.name, uploaded_image)
        upload_file_url = '/images/' + str(request.user.id) + "/uploads/" + file_name

        diagnosis = compute_result.process_image(upload_directory, result_directory, file_name)
        processed_file_url = '/images/' + str(request.user.id) + "/results/" + file_name

    user = None
    if request.user.is_authenticated:
        user = request.user
    prediction = Prediction.objects.create(
        user=user,
        diagnosis=diagnosis,
        uploaded_image_url=upload_file_url,
        processed_image_url=processed_file_url,
    )
    context = {
        'prediction': prediction
    }
    return render(request, 'main/result.html', context)


@require_http_methods(['GET'])
def history(request):
    print(request.user)
    predictions = Prediction.objects.filter(user=request.user)
    print(predictions)
    context = {
        'predictions': predictions
    }
    return render(request, 'main/history.html', context)
