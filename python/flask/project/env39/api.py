from flask import Flask, render_template, make_response, jsonify, url_for, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "mydb"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


def data_fetch(query, params=None):
    cur = mysql.connection.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data


@app.route("/party", methods=["GET"])
def getParty():
    data = data_fetch("""SELECT * FROM party""")
    return render_template('index.html', party=data)


@app.route("/party/<int:id>/staff", methods=["GET"])
def getPartyStaff(id):
    data = data_fetch(
        """
        SELECT party.idparty, party.party_type, roles.role_detail, staff.staff_details
        FROM party
        LEFT JOIN roles ON party.idparty = roles.idrole
        LEFT JOIN staff ON party.idparty = staff.idstaff
        WHERE party.idparty = %s
    """,
        (id,),
    )
    return make_response(
        jsonify({"idparty": id, "staff_details": data}),
        200
    )


@app.route("/party", methods=["POST"])
def addParty():
    cur = mysql.connection.cursor()
    info = request.get_json()
    party_type = info["party_type"]
    # last_name = info["last_name"]
    cur.execute(
        """ INSERT INTO party (party_type) VALUE (%s, %s)""",
        (party_type),
    )
    mysql.connection.commit()
    print("row(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "party added successfully", "rows_affected": rows_affected}
        ),
        201,
    )


@app.route("/party/<int:id>", methods=["PUT"])
def updateParty(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    party_type = info["party_type"]
    # last_name = info["last_name"]
    cur.execute(
        """ UPDATE actor SET party_type = %s WHERE actor_id = %s """,
        (party_type, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "party updated successfully",
                "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/party/<int:id>", methods=["DELETE"])
def deleteParty(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM actor where idparty = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "party deleted successfully",
                "rows_affected": rows_affected}
        ),
        200,
    )


@app.route("/party/format", methods=["GET"])
def getPartyParams():
    fmt = request.args.get('id')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format": fmt, "foo": foo}), 200)


if __name__ == "__main__":
    app.run(debug=True)
