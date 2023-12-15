from flask import Flask, jsonify, request
from sqlalchemy import text
from db_config import get_session

app = Flask(__name__)


@app.route("/todos", methods=["GET", "POST"])
def handle_todo():
    with get_session() as session:
        if request.method == "GET":
            result = session.execute(text("SELECT * FROM todos;"))
            todos = [{"id": row[0], "description": row[1]} for row in result]
            return jsonify(todos)
        elif request.method == "POST":
            data = request.json
            session.execute(
                text("INSERT INTO todos (description) VALUES (:description);"),
                {"description": data["description"]},
            )
            return jsonify({"message": "Todo added!"}), 201


if __name__ == "__main__":
    app.run(debug=True)



