import os
from flask import Flask, flash, request, redirect, url_for
from myapp.models.file_loader import FileLoader
from myapp.models.file_converter import FileConverter

def post_upload(app,request):

    # проверим, передается ли в запросе файл 
    if 'file' not in request.files:
        flash('Не могу прочитать файл')
        return redirect(request.url)

    file = request.files['file']

    # Если файл не выбран
    if file.filename == '':
        flash('Нет выбранного файла')
        return redirect(request.url)
        
    file_path = FileLoader.save_from_temp(app.config['UPLOAD_FOLDER'] , file)

    #FileConverter.convert_to(app,file_path,"WEBP")


    return redirect(request.url)
    #return redirect(url_for('download_file', name=filename))

