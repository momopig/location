from flask import Flask
from flask import request
from flask import render_template
import os
from threading import Lock
app = Flask(__name__, static_folder='')

lock = Lock()

@app.route('/note')
def note():
    lng = request.values.get('lng')
    lat = request.values.get('lat')
    if lng is not None and lat is not None:
        with lock:
            f = open('./noteLocation.gpx', 'w')
            f.write('<gpx creator="Xcode" version="1.1"><wpt lat="%s" lon="%s"><name>PokemonLocation</name></wpt></gpx>' % (lat, lng))
            f.close()
            os.system('osascript clickMenu.applescript')
        return '{"suc":1, "lng":"%s", "lat":"%s"}' % (lng, lat)
    return '{"suc":0}'

@app.route('/')
def index():
    return app.send_static_file('po-go.html')

app.run('0.0.0.0', 5000, debug=True)

