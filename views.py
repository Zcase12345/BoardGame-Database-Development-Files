#this file will store all of our URL "endpoints"

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

#if we type / into our URL it will display the home page
@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1: 
            flash('Board game description is too short!', category='error')
        else: 
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Board game added!', category='success')
    return render_template("home.html", user=current_user)     #this will render the home.html file now with the render_template function 

@views.route('/delete-note', methods=['POST'])
def delete_note(): 
    note = json.loads(request.data)
    noteID = note['noteID']
    note = Note.query.get(noteID)
    if note: 
        if note.user_id == current_user.id: 
            db.session.delete(note)
            db.session.commit()
    return jsonify({})