from flask import Flask, make_response, render_template
import datetime
from functions import *
import pathlib

app = Flask(__name__)

basedir = pathlib.Path(__file__).parent.resolve()

def cookie_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'session_id' not in request.cookies:
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def start_page():
    ''' beginning page in process, start a folder and get initial choices '''

    # get timestamp and convert to string so it can be used to save data to same folder
    temp_timestamp = str(datetime.datetime.now())
    timestamp = simplify_timestamp(temp_timestamp)


    resp = make_response(render_template('home.html', timestamp=timestamp))
    resp.set_cookie('session_id', timestamp)

    #return render_template('login_form.html', alert_box_class=alert_box_class, results=results)
    # return render_template('login_form.html', alert_box_class=alert_box_class, results=results, resp=resp)
    return resp

if __name__ == '__main__':
    # app.run()
    app.run(debug=True, host='0.0.0.0')
