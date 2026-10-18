
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = None
    num1 = ""
    num2 = ""
    operation = "+"

    if request.method == "POST":
        num1 = request.form.get("num1", "").strip()
        num2 = request.form.get("num2", "").strip()
        operation = request.form.get("operation", "+")

        try:
            a = float(num1)
            b = float(num2)

            if operation == "+":
                result = a + b

            elif operation == "-":
                result = a - b

            elif operation == "*":
                result = a * b

            elif operation == "/":
                if b == 0:
                    error = "Cannot divide by zero!"
                else:
                    result = a / b

            else:
                error = "Invalid operation!"

        except ValueError:
            error = "Please enter valid numbers."

    return render_template(
        "index.html",
        result=result,
        error=error,
        num1=num1,
        num2=num2,
        operation=operation
    )


if __name__ == "__main__":
    app.run(debug=True)
