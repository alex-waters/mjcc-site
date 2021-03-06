import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def send_wheel():
    page = render_template('info_page.html')
    return page

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

if __name__ == '__main__':
    app.run()
