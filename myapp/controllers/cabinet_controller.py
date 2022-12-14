from myapp import app , db
from flask import Flask ,render_template , flash, request, redirect, url_for 
from flask_login import  login_user, current_user , logout_user
from myapp.forms.login import LoginForm
from myapp.models.user import User
from myapp.models.parse_seanse import Parse_seanse

def get_cabinet(app,request):

    seanses = Parse_seanse.get_all_for_user_id( current_user.id)
    
    if(seanses is None ):
        seanses = []
    return render_template("cabinet.html" , seanses=seanses)
    