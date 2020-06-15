# DailyLog form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms import SelectMultipleField, DecimalField, SelectField
from wtforms.validators import DataRequired
from wtforms.widgets import html_params


def select_multi_checkbox(field, ul_class='', **kwargs):
        kwargs.setdefault('type', 'checkbox')
        field_id = kwargs.pop('id', field.id)
        html = [u'<ul %s>' % html_params(id=field_id, class_=ul_class)]
        for value, label, checked in field.iter_choices():
            choice_id = u'%s-%s' % (field_id, value)
            options = dict(kwargs, name=field.name, value=value, id=choice_id)
            if checked:
                options['checked'] = 'checked'
            html.append(u'<li><input %s /> ' % html_params(**options))
            html.append(u'<label for="%s">%s</label></li>' % (field_id, label))
        html.append(u'</ul>')
        return u''.join(html)


class DailyLogForm(FlaskForm):
    '''
        Add DailyLog Form
    '''

    temp_ini = DecimalField('Temperatura Inicial', places=1, rounding=None,
                            validators=[DataRequired()])
    temp_final = DecimalField('Temperatura Final', places=1, rounding=None,
                              validators=[DataRequired()])
    type_tx = SelectField('¿Que medio de transporte utilizaste hoy?',
                          choices=[('Ninguno', 'Ninguno'),
                                   ('Público', 'Público'),
                                   ('Particular', 'Particular')],
                          validators=[DataRequired()])
    sintomas = SelectMultipleField('Sintomas', widget=select_multi_checkbox)
