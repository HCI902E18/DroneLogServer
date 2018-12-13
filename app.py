import os
from os import path

from flask import Flask, render_template, jsonify

from LogFile import LogFile
from LogFiles import LogFiles

app = Flask(__name__)


@app.route('/')
def home():
    confirmed = [
        '[21-11-2018][09.18.45]',
        '[21-11-2018][09.18.40]',
        '[21-11-2018][09.18.29]',
    ]
    folders = [folder for folder in LogFiles().folders() if folder in confirmed]

    return render_template(
        'map.html',
        files=folders
    )


@app.route('/log/<string:folder>')
def log(folder):
    file = LogFile(folder)

    return jsonify(file.data())


if __name__ == '__main__':
    extra_dirs = ['./templates/', './static/', ]
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = path.join(dirname, filename)
                if path.isfile(filename):
                    extra_files.append(filename)
    app.run(
        debug=True,
    )
