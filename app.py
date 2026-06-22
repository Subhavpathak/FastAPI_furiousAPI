from flask import Flask, request

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>Table Generator</title>
<h2>Multiplication Table Demo</h2>
<form method="get">
  <input type="number" name="number" placeholder="Enter a number" value="{value}">
  <button type="submit">Show Table</button>
</form>
<pre>{table}</pre>
"""

@app.route("/")
def show_table():
    number = request.args.get("number", "")
    table = ""
    if number:
        try:
            n = int(number)
            table = "\n".join(f"{n} x {i} = {n*i}" for i in range(1, 11))
        except ValueError:
            table = "Please enter a valid integer."
    return PAGE.format(value=number, table=table)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)