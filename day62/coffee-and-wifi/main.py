from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv, data_manager

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
csrf = CSRFProtect(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe location on Google Maps (URL)', validators=[DataRequired()])
    open_time = StringField('Opening Time e.g.10AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g.5:30pM', validators=[DataRequired()])
    coffee_rating = StringField('Coffee Rating', validators=[DataRequired()], render_kw={"list": "suggestions_for_coffee", "autocomplete": "off"})
    wifi_rating = StringField('WiFi Rating', validators=[DataRequired()], render_kw={"list": "suggestions_for_wifi", "autocomplete": "off"})
    power_socket = StringField('Power Socket Availability', validators=[DataRequired()], render_kw={"list": "suggestions_for_power_socket", "autocomplete": "off"})
    submit = SubmitField('Submit')

# Exercise:
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    suggestions_for_wifi = ['✘','💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪💪']
    suggestions_for_coffee = ['✘','☕️','☕️☕️','☕️☕️☕️','☕️☕️☕️☕️','☕️☕️☕️☕️☕️']
    suggestions_for_power_socket = ['✘','🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌']
    form = CafeForm()
    if form.validate_on_submit():
        data_manager.set_data_to_csv(form)
        return redirect(url_for('add_cafe', form=form))

    return render_template('add.html',
                           form=form,
                           suggestions={
                               "wifi": suggestions_for_wifi,
                               "coffee": suggestions_for_coffee,
                               "power_socket": suggestions_for_power_socket}
                           )


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
