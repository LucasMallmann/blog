import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
from flaskblog.models import User

def save_picture(form_picture) -> str:
    '''
        It's going to save a picture to the static directory
    '''
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_filename)

    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    form_picture.save(picture_path)
    return picture_filename


def send_reset_email(user: User):
    token = user.get_reset_token()
    message = Message('Password reset request', 
                        'lucasmallmann76@gmail.com',
                        recipients=[user.email])
    message.body = f''' To reset yout password, follow the link:
{url_for('users.reset_token', token=token, _external=True)}
'''
