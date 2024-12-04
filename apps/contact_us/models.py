import datetime
from .common import db, Field, auth
from pydal.validators import *

def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()

db.define_table(
    'contact_requests',
    Field('name', 'string', requires=IS_NOT_EMPTY(), label='Name'),
    Field('email', 'string', requires=IS_EMAIL(), label='Email'),
    Field('phone', 'string', requires=IS_NOT_EMPTY(), label='Phone'),
    Field('message', 'text', label='Message'),
    Field('created_at', 'datetime', default=get_time, writable=False, readable=False),
)

db.commit()

