from flask import (
    Blueprint, render_template, request, url_for, redirect, flash
    )

from . import models
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from app import db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User(username, generate_password_hash(password))

        print(f"{username}, ' ', {password}")

        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('auth.login'))
        
    return render_template('auth/register.html')

@bp.route('/login')
def login():
    return render_template('auth/login.html')