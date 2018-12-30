from flask import Flask, jsonify
import re

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

def validate_users(json):
    if not(json["username"].strip()):
        return jsonify({"Message":"Username is required"}), 401

    if not (json["email"].strip()):
        return jsonify({"Message":"Email is required"}), 401

    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", json["email"].strip()) is None:
        return jsonify({"Message":"Invalid email"}), 401

    if not (json["password"].strip()):
        return jsonify({"Message":"Password is required"}), 401

    if (len(json["password"].strip()) < 8 or len(json["password"].strip()) > 12):
        return jsonify({"Message":"Password length should be atleast 8 characters long and atmost 12 characters long"}), 401

    if not (json["confirm"].strip()):
        return jsonify({"Message":"Password confirmation is required"}), 401

    if not (json["password"].strip() == json["confirm"].strip()):
        return jsonify({"Message":"Password mismatch"}), 401

    return True
