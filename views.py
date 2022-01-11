from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import FileUploadForm
from django.contrib import messages
from myapp.models import TextFile
from myapp.textpy import textpy
from django.http import FileResponse
import os


def index(request):
    all_data = TextFile.objects.all()
    context = {
        'title': 'テキストマイニングツール',
        'all_data': all_data,
    }
    return render(request, 'index.html', context)


def upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'アップロードに成功しました')
            return redirect('index')
    else:
        form = FileUploadForm()
        
    context = {
        'title': 'アップロード画面',
        'form': form,
    }
        
    return render(request, 'upload.html', context)


def download(request, id):
    download_data = get_object_or_404(TextFile, pk=id)
    file_path = download_data.file.url
    result_path = textpy(file_path[1:])
    return FileResponse(open(result_path, "rb"), as_attachment=True)


def delete(request, id):
    delete_data = get_object_or_404(TextFile, pk=id)
    delete_file =  delete_data.file.url
    delete_png_file = delete_file[:-3] + 'png'
    
    try:
        os.remove(delete_png_file[1:])
    except:
        messages.success(request, '一度ダウンロードしてから削除してください')
        return redirect('index')
    else:
        os.remove(delete_file[1:])
        delete_data.delete()
        messages.success(request, 'データを削除しました')
        return redirect('index')
    