from flask import Flask, render_template, redirect, request
from forms import contactForm, subscribeEmail
import os

app = Flask(__name__)
cat = os.urandom(24)
app.config['SECRET_KEY'] = cat

#contact and subscribe form
@app.route('/', methods=['GET', 'POST'])
def index():
    form1 = contactForm()
    form2 = subscribeEmail()
    work = ['Web Design', 'Psd to html', 'Web hosting', 'website template']
    if form1.is_submitted and form1.validate():
        return redirect('/contact')
    elif form2.is_submitted:
        if request.method == 'POST':
            return redirect('/about')
    return render_template('index.html', form1=form1, work=work, form2=form2)

#subscribe form
@app.route('/about', methods=['GET', 'POST'])
def about():
    forms = subscribeEmail()
    if request.method == 'POST':
        return redirect('/contact')
    return render_template('about.html', forms=forms)

#contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = contactForm()
    if request.method == 'POST':
        return redirect('/')
    return render_template('contact.html')

#subscribe form
@app.route('/projects', methods=['GET', 'POST'])
def projects():
    form = subscribeEmail()
    if request.method == 'POST':
        return redirect('/')
    return render_template('projects.html', form=form)

#subscribe form
@app.route('/services', methods=['GET', 'POST'])
def services():
    form = subscribeEmail()
    if request.method == 'POST':
        return redirect('/support')
    return render_template('services.html', form=form)

#contact form
@app.route('/support', methods=['GET', 'POST'])
def support():
    form = contactForm()
    if request.method == 'POST':
        return redirect('/')
    return render_template('support.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)