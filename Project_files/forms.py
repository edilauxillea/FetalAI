from flask_wtf import  FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import InputRequired

class input(FlaskForm):
    a = FloatField("Baseline Value", validators=[InputRequired()])
    b = FloatField("Fetal Movement", validators=[InputRequired()])
    c = FloatField("Light Decelerations", validators=[InputRequired()])
    d = FloatField("Severe Decelerations", validators=[InputRequired()])
    e = FloatField("Prolonged Decelerations", validators=[InputRequired()])
    f = FloatField("Abnormal Short Term Variability", validators=[InputRequired()])
    g = FloatField("Mean value of Short term Variability", validators=[InputRequired()])
    h = FloatField("Percentage Of times with Abnormal Long term Variability", validators=[InputRequired()])
    i = FloatField("Mean value of Long term Variability", validators=[InputRequired()])
    j = FloatField("Histogram Minimum value", validators=[InputRequired()])
    k = FloatField("Histogram Maximum value", validators=[InputRequired()])
    l = FloatField("Histogram Mode value", validators=[InputRequired()])
    m = FloatField("Histogram Variance value", validators=[InputRequired()])
    submit = SubmitField("Submit Readings")
