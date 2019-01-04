from flask import Flask, Response, request, render_template
import json
app = Flask(__name__)
import math

@app.route('/', methods=['GET'])
def inverseSquare():
    distance = request.args.get('distance')
    if distance == None:
        return Response(json.dumps({'message': "You must specify a distance for the inverse square law"}), mimetype='application/json', status='400')
    else:
        try:
            return Response(json.dumps(
                {"signal-strength": 1/(float(distance)**2)}
            ), mimetype='application/json', status='200')
        except:
            return Response(json.dumps({'message': "Error distance must be a number"}), mimetype='application/json', status='400')
            

if __name__ == '__main__':
    app.run(debug=True)