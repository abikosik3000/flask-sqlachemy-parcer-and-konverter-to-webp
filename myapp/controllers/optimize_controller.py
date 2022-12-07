import os
import uuid
from flask import Flask, flash, request, redirect, url_for , render_template
from myapp.models.file_loader import FileLoader
from myapp.models.file_converter import FileConverter
from myapp.models.parser import Parser

PARSE_FOLDER_NAME = "parser_load"

def post_upload_from_site(app,request):

    if(request.form.get("site") == ""):
        flash("Введите название сайта")
        return redirect(request.url)

    page_to_parse = request.form.get("site")

    urls = Parser.get_all_images(page_to_parse)
    save_urls = []
    parse_id = str( uuid.uuid4() )
    for url in urls:
        buff = FileLoader.save_from_url(
                app.config['UPLOAD_FOLDER'] +"/"+PARSE_FOLDER_NAME+"/"+parse_id ,url)
        if(not (buff is None)):
            save_urls.append( buff)

    

    print(save_urls)
    for path in save_urls:

        _filename_save = path.split("/")[-1]
        _upload_folder = app.config['UPLOAD_FOLDER'] +"/"+PARSE_FOLDER_NAME+"/"+parse_id+"/optimized"
        FileConverter.convert_to(_upload_folder,path,"WEBP", filename_save=_filename_save)
    

    
    return redirect(request.url)
    #return render_template('upload_from_site.html')
