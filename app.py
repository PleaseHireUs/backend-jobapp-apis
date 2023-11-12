from flask import Flask, jsonify, request
from JobAppData import JobAppData
from data import JobAppDao
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Route to insert jobAppData
@app.route('/addJobApps', methods=['POST'])
def insert_jobapp():
    if not request.json or 'emailId' not in request.json:
        return jsonify({'error': 'The emailId is required'}), 400

    jobApp = JobAppData(
        userId = request.json['userId'],
        platform= request.json['platform'],
        companyName= request.json['companyName'],
        jobTitle= request.json['jobTitle'],
        createdDate= request.json['createdDate'],
        jobStatus= 'Submitted',
        emailId= request.json['emailId'],
        jobUrl= request.json['jobUrl']
    )
    insertResposne = JobAppDao().insert_jobapp(jobApp)
    return jsonify(insertResposne), 200

# Route to add a new task
@app.route('/jobApps', methods=['POST'])
def get_all_jobs():
    if not request.json or 'emailId' not in request.json:
        return jsonify({'error': 'The emailId is required'}), 400

    jobApp = JobAppDao().find_all_jobapp(request.json['userId'],
                                        request.json['emailId'], 
                                        request.json['skip'],
                                        request.json['limit'],
                                        request.json['sortfields'])
    return jsonify(jobApp), 200

# Route to update the status of a task
@app.route('/updateJobStatus/', methods=['POST'])
def update_status():
    if not request.json or 'emailId' not in request.json:
        return jsonify({'error': 'The emailId is required'}), 400

    jobApp = JobAppData(
        userId = request.json['userId'],
        platform= request.json['platform'],
        companyName= request.json['companyName'],
        jobTitle= request.json['jobTitle'],
        modifiedDate = request.json['modifiedDate'],
        jobStatus= request.json['jobStatus'],
        emailId= request.json['emailId'],
        jobUrl= request.json['jobUrl']
    )
    insertResposne = JobAppDao().insert_jobapp(jobApp)
    if insertResposne is None:
        return jsonify("could not find the application"), 404
    return jsonify(insertResposne), 200


if __name__ == '__main__':
    app.run(debug=True)
