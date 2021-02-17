""" unit conversion to SI """

from flask import Flask, request, jsonify
from convert_unit.convert_unit import ConvertUnit

app = Flask(__name__)

@app.route('/units/si', methods=['GET'])
def get_converted_si_unit():
    """ Method to take input request and return the result """
    units = request.args.get('units')
    response = ConvertUnit(units).convert()
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    