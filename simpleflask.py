from flask import Flask, jsonify, request

app = Flask(__name__)


from sqlalchemy import create_engine

engine = create_engine("postgres", echo=True)


@app.route("/", methods=["GET", "POST", "PUT"])
def get_example():
    if request.method == "GET":
        return jsonify({"message": "This is a GET response!"})
    elif request.method == "PUT":
        return jsonify({"message": "This is a PUT response!"})
    else:
        return jsonify({"error": "Method not supported!"})
    



@app.route("/users", methods=["GET", "POST", "PUT"])
def get_users():
    return jsonify({"message": "This is a USERS endpoint response!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
