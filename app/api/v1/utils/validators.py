from flask import Flask, jsonify

def validate_question(json):
    if not(json["qntitle"].strip()):
        return jsonify({"Message":"Question title is required"}), 401

    if not (json["qntags"].strip()):
        return jsonify({"Message":"Question tag(s) is required"}), 401

    if not (json["qnbody"].strip()):
        return jsonify({"Message":"Question body is required"}), 401

    return True

def validate_answer(json):
    if not(json["ansbody"].strip()):
        return jsonify({"Message":"Answer field cannot be blank!"}), 401

    return True    
