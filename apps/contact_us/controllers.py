from py4web import action, request, abort, redirect, URL
from yatl.helpers import A
from .common import db, session, T, cache, auth, logger, authenticated, unauthenticated, flash
from py4web.utils.url_signer import URLSigner
from .models import get_user_email
from py4web.utils.form import Form, FormStyleBulma
from py4web.utils.grid import Grid, GridClassStyleBulma

# Complete. 
@action('index', method=['GET', 'POST'])
@action.uses('index.html', db, session, T)
def index():
    form = Form(db.contact_requests, csrf_session=session, formstyle=FormStyleBulma)
    if form is None:
        print("Error")
    else:
        print("Success")
    if form.accepted:
        redirect(URL('index'))
    return dict(form=form)

@action('contact_requests', method=['GET', 'POST'])
@action.uses(auth.user, 'contact_requests.html', db, session, T)
def contact_requests():
    if auth.current_user.get('email') != 'admin@example.com':
        redirect(URL('index'))
    grid = Grid(db.contact_requests, orderby=~db.contact_requests.id, grid_class_style=GridClassStyleBulma)
    return dict(grid=grid)
