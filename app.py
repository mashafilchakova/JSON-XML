from flask import Flask, request
import xmltodict


app = Flask(__name__)


@app.route('/json/to/xml/v1.0', methods=['POST'])
def convert():
    """
    Convert xml data to dictionary format and then dump to YAML format
    :return:
    YAML message
    """
    d = request.get_json()
    return xmltodict.unparse(d), 201



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
