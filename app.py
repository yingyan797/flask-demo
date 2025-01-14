from flask import Flask, request, render_template

app = Flask("__name__")

@app.route("/", methods=["get", "post"]) 
def index(): 
    fm = request.form
    print(fm)
    n1 = fm.get("n1")
    n2 = fm.get("n2")
    result = ""
    like_python = ""
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
                if float(n2) == 0:
                    result = "Can't divide by zero"
                else:
                    result = float(n1) / float(n2)
        result = f"{n1} {op} {n2} = {result}"
    if lp:=fm.get("likepython"):
        match lp:
            case "yes":
                like_python = 100
            case "no":
                like_python = 0
            case _:
                like_python = 50

    return render_template("index.html", result=result, like=like_python)

@app.route("/database", methods=["get", "post"]) 
def database(): 
    return render_template("database.html")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)