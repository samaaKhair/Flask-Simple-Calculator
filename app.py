from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def calculator():
  if request.method == "POST":
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    if "operation" in request.form: 
      operation = request.form["operation"]
    else:
      operation = None  


    if operation == "+":
      result = num1 + num2
    elif operation == "-":
      result = num1 - num2
    elif operation == "*":
      result = num1 * num2
    elif operation == "/":
      if num2 == 0:
        result = "Error: Division by zero"
      else:
        result = num1 / num2
    else:
      result = "Invalid operation"
  else:
    result = None
  return render_template("index.html", result=result)

if __name__ == "__main__":
  app.run(debug=True)
