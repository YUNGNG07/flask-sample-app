'''
Websites that might help:
Flask:                  https://flask.palletsprojects.com/en/3.0.x/
HTML Syntax:            https://www.w3schools.com/html/default.asp
HTML Forms and Buttons: https://www.w3schools.com/html/html_forms.asp
'''

# Python module to create Flask app
import flask

# Creates a Flask application object (instance)
# Uses it to know where to get the HTML templates, static files required to run the application
app = flask.Flask(__name__)
# Add secret key to use flash message function
app.secret_key = '123'

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    Create a main page

    Notes:
        GET : retrieve information from website
        POST: send information to website
    '''
    if flask.request.method == 'POST':
        # If the password entered by user is not equal to 123
        # Get password information from HTML text input with the name 'pin'
        if flask.request.form.get('pin') != '123':
            # Display error message
            flask.flash('Wrong pin!', 'error')
        # If password is correct
        else:
            # If user press on the HTML submit button with the name 'Hello'
            if flask.request.form.get('Hello') == 'Hello':
                # Display welcome message
                flask.flash('Say hi!')
        # Runs the HTML template file to display webpage UI
        return flask.render_template('index.html')
    # If user refreshes the website page
    elif flask.request.method == 'GET':
        return flask.render_template('index.html')

# Run the flask app
if __name__ == '__main__':
    '''
    Settings:
        host        : URL domain to run Flask app
        debug       : Enable built-in debugger for Flask
        use_reloader: Disable auto-reloader that refreshes the HTML website whenever code is modified
    '''
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
