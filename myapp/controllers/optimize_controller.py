import os
import uuid
from myapp import db
from flask import Flask, flash, request, redirect, url_for , render_template
from myapp.models.file_loader import FileLoader
from myapp.models.file_converter import FileConverter
from myapp.models.parser import Parser
from myapp.models.parse_seanse import Parse_seanse
from myapp.models.file import File
from sqlalchemy import select


PARSE_FOLDER_NAME = "parser_load"

def get_upload_from_site(app,request):

    parse_seanse_id = request.args.get('parse_seanse_id')
    
    query = File.query.filter(File.parse_seanse_id == parse_seanse_id).all()
    print(query)

    return render_template('upload_from_site.html' , images=query)

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
            os.path.join( PARSE_FOLDER_NAME , parse_id)
            , url)

        if(not (buff is None)):
            save_urls.append( buff)

    seanse = Parse_seanse()
    db.session.add(seanse)
    db.session.commit()
    
    for path in save_urls:

        _filename_save = path.split("/")[-1]
        _upload_folder = os.path.join(PARSE_FOLDER_NAME, parse_id,"optimized")
        FileConverter.convert_to(_upload_folder,path,"WEBP"
        , filename_save=_filename_save , parse_seanse_id=seanse.id)
        

    return redirect( url_for('get_optimize' ,parse_seanse_id = seanse.id) )
    #return render_template('upload_from_site.html')
