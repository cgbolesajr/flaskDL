from flask import Flask

app = Flask(__name__)


@app.route('/sample')
def running():
    return 'flask is running'
    
if __name__ == '__main__':
    print('Starting Flask')
    app.run()
    # or
    ## at sh/cmd 
    ## linux --> export FLASK_APP=sample_app.py
    # windows --> C:\path\to\app set FLASK_APP=sample_app.py
    # env --> $env:FLASK_APP="sample_app.py"
    # flask run --host=0.0.0.0
