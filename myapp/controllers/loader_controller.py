import uuid
import os
from flask import Flask, flash, request, redirect, url_for

def file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

def allowed_file(filename):
    return '.' in filename and file_extension(filename) in ALLOWED_EXTENSIONS

# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def upload_post(app,request):
    
    # проверим, передается ли в запросе файл 
    if 'file' not in request.files:
        flash('Не могу прочитать файл')
        return redirect(request.url)

    file = request.files['file']

    # Если файл не выбран
    if file.filename == '':
        flash('Нет выбранного файла')
        return redirect(request.url)

    if file and allowed_file(file.filename):

        filename = str(uuid.uuid4()) + '.'+file_extension(file.filename)

        # сохраняем файл
        #app.config['UPLOAD_FOLDER'] , 
        file.save(app.config['UPLOAD_FOLDER'] + "/"+filename  )
        
        return redirect(request.url)
        #return redirect(url_for('download_file', name=filename))