from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__)
app.secret_key = "your_secret_key"




# Replace with your actual settings
MS_IDENTITY_WEB = None
AAD_CONFIG = None

# Define your views here


@app.route('/index/')
def index():
    # get_full_name = request.identity_context_data.username
    # context = {'get_full_name': get_full_name}
    context = {'get_full_name': 'get_full_name'}
    return render_template('azure_ad_api/index.html', **context)


@app.route('/')
def login_user():
    return render_template('azure_ad_api/login.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True,)
