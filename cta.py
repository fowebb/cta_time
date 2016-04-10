from flask import Flask, url_for
import requests
from bs4 import BeautifulSoup
from env import CTA_API_KEY
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return "MAIN LANDING PAGE"


@app.route("/arrivals")
def api_arrivals():
    return url_for('api_arrivals')


@app.route("/arrivals/<stationid>")
def api_arrival(stationid):
    """
    Receives station, pings CTA Train Tracker API, and returns arrival times for specified station
    """
    stations = {
        'south': {
            'map_id': 40840,
            'stop_id': 30164,
            'name': 'South Boulevard'},
        'belmont': {
            'map_id': 41320,
            'stop_id': 30257,
            'name': 'Belmont'},
        'randolph': {
            'map_id': 40200,
            'stop_id': 30039,
            'name': 'Randolph/Wabash'}
    }

    if stationid not in stations.keys():
        raise Exception("Unknown station name!")

    params = {
        'key': CTA_API_KEY,
        'mapid': stations[stationid]['map_id'],
        'stpid': stations[stationid]['stop_id']
    }

    # CTA Train Tracker API url
    BASE_URL = "http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?"

    # Fetch data and throw it into beautifulsoup
    r = requests.get(BASE_URL, params=params)
    soup = BeautifulSoup(r.text)

    results = []
    for eta in soup.find_all('eta'):
        # Only care about purple line
        line = eta.find('rt').text
        if line != 'P':
            continue
        line = 'Purple'
        # Strip route direction
        station = eta.find('stanm').text
        stop = eta.find('stpde').text
        # Strip times and calculate minutes to arrival
        arrival_time = datetime.strptime(eta.find('arrt').text, "%Y%m%d %H:%M:%S")
        request_time = datetime.strptime(eta.find('prdt').text, "%Y%m%d %H:%M:%S")
        time_to_arrival = arrival_time - request_time
        seconds = time_to_arrival.total_seconds()
        minutes = int((seconds % 3600) / 60)
        results.append("{} ({}): {} minutes".format(line, stop, minutes))
    return ' | '.join(results)


if __name__ == "__main__":
    app.run()
