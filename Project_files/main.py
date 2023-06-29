from flask import  Flask, render_template, request, redirect
from forms import input
from model import Get_Data, Scale, model
app = Flask(__name__)
app.config["SECRET_KEY"] = "abcd"

@app.route("/", methods = ["POST", "GET"])
def home():
    form = input()
    if form.is_submitted():
        result = request.form
        result = Get_Data(result)
        result = Scale(result)
        result = model.predict(result)
        conditions = {"1.0" :"Normal",
                      "2.0" : "Suspect",
                      "3.0" : "Pathological"}
        result = conditions[result[0]]
        return render_template("result.html", result=result)
    return render_template("test.html", form=form)
if __name__ == "__main__":
    app.run(debug=True)
