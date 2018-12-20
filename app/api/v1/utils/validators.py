from flask import Flask, jsonify

def validate_user(json):
    if not(json["username"].strip()):
        return jsonify({"Message":"A username is required!"}), 401

    if not(json["email"].strip()):
        return jsonify({"Message": "Email Address required!"}), 401

    if not(json["password"].strip()):
        return jsonify({"Message": "Password required!"}), 401

    if not(json["retype_password"].strip()):
        return jsonify({"Message": "Retype password to confirm match!"}), 401

    if (json["password"].strip() != json["retype_password"].strip()):
        return jsonify({"Message": "Both passwords must match!"}), 401

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
