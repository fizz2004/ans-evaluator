from flask import Flask, request, jsonify
from main import knowledge_assessment

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    job_role = data.get("job_role")
    resume = data.get("resume")
    user_responses = data.get("user_responses")

    if not job_role or not resume or not user_responses:
        return jsonify({"error": "Missing fields"}), 400

    score = knowledge_assessment(job_role, resume, user_responses)
    return jsonify({"knowledge_score": score})

if __name__ == "__main__":
    app.run(debug=True)
