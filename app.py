from flask import Flask, request, render_template

app = Flask("__name__")

@app.route("/", methods=["get", "post"]) 
def index(): 
    fm = request.form
    n1 = fm.get("n1")
    n2 = fm.get("n2")
    result = ""
    if fm.get("calculate") and n1 and n2:
        op =  fm.get("operator")
        match op:
            case "+":
                result = float(n1) + float(n2)
            case "-":
                result = float(n1) - float(n2)
            case "*":
                result = float(n1) * float(n2)
            case "/":
                result = float(n1) / float(n2)
    return render_template("index.html", result=f"{n1} {op} {n2} = {result}")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)