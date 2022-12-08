import os
import uuid
from myapp import db
from flask import Flask, flash, request, redirect, url_for , render_template
from myapp.models.file_loader import FileLoader
from myapp.models.file_converter import FileConverter
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

    seanse = Parse_seanse()
    db.session.add(seanse)
    db.session.commit()
    seanse.convert_all_img_from_url(page_to_parse)
    
    return redirect( url_for('get_optimize' ,parse_seanse_id = seanse.id) )
    #return render_template('upload_from_site.html')
