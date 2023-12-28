from flask import Flask, render_template, make_response, jsonify, url_for, redirect, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "mydb"

app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mydb.party")
    party = cur.fetchall()
    cur.close()

    return render_template('index.html')


@app.route("/edit/<int:idparty>", methods=["GET", "POST"])
def edit(party_type):
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        party_type = request.form['party_type']
        cur.execute("UPDATE party SET party_type=%s WHERE id=%s",
                    (party_type, id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))
    else:
        cur.execute("SELECT * FROM party WHERE id = %s", (id,))
        institutions = cur.fetchone()
        cur.close()

        return redirect(url_for('index'))


def delete(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM party WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
