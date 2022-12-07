import os
import uuid
from flask import Flask, flash, request, redirect, url_for , render_template
from myapp.models.file_loader import FileLoader
from myapp.models.file_converter import FileConverter
from myapp.models.parser import Parser

PARSE_FOLDER_NAME = "parser_load"

def post_upload_from_site(app,request):

    urls = Parser.get_all_images("http://abikosru.beget.tech/")
    save_urls = []
    parse_id = str( uuid.uuid4() )
    for url in urls:
        save_urls.append( 
            FileLoader.save_from_url(
                app.config['UPLOAD_FOLDER'] +"/"+PARSE_FOLDER_NAME+"/"+parse_id ,url) )

    for path in save_urls:

        _filename_save = path.split("/")[-1]
        _upload_folder = app.config['UPLOAD_FOLDER'] +"/"+PARSE_FOLDER_NAME+"/"+parse_id+"/optimized"
        FileConverter.convert_to(_upload_folder,path,"WEBP", filename_save=_filename_save)
    

    #TODO
    return redirect(request.url)
    #return render_template('upload_from_site.html')
