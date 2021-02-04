from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
# print(__name__)


@app.route('/')
def hello_world():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_file = database.write(
            f'\n Email:{email},\n Subject:{subject},\n Message:{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        Email = data['email']
        Subject = data['subject']
        Message = data['message']

        csv_witer = csv.writer(
            database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_witer.writerow([Email, Subject, Message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong please try again later'


# @app.route('/index.html')
# def home():
#     return render_template('./index.html')
# @app.route('/works.html')
# def works():
#     return render_template('./works.html')
# @app.route('/about.html')
# def about():
#     return render_template('./about.html')
# @app.route('/contact.html')
# def contacts():
#     return render_template('./contact.html')
# @app.route('/components.html')
# def components():
#     return render_template('./components.html')
