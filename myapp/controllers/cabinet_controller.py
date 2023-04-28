from flask import render_template
from flask_login import current_user

from myapp import app, db
from myapp.models.parse_seanse import Parse_seanse


def get_cabinet(app, request):

    seanses = Parse_seanse.get_all_for_user_id(current_user.id)

    if seanses is None:
        seanses = []
    return render_template("cabinet.html", seanses=seanses)
