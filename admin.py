from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

admin = Admin(app, name='Resume Builder Admin', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Resume, db.session))
