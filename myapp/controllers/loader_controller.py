from flask import flash, redirect

from myapp.models.file_loader import FileLoader


def post_upload(app, request):

    # проверим, передается ли в запросе файл
    if "file" not in request.files:
        flash("Не могу прочитать файл")
        return redirect(request.url)

    file = request.files["file"]

    # Если файл не выбран
    if file.filename == "":
        flash("Нет выбранного файла")
        return redirect(request.url)

    file_path = FileLoader.save_from_temp(file)

    return redirect(request.url)
