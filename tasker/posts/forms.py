from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class NewPostForm(FlaskForm):
    """Create blog post Form"""
    body = TextAreaField('Post Body', validators=[DataRequired()])
    submit = SubmitField('Publish')
