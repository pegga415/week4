from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key = "#230dec61-fee8-4ef2-a791-36f9e680c9fc"

# 首頁
@app.route('/')
def index():
    if "user" in session:
        return redirect(url_for("member")) 
    return render_template('index.html')


# 登入頁
@app.route("/signin", methods=["POST","GET"])
def signin():
    if request.method == "POST":
        user = request.form["userID"]
        password = request.form["password"]
        session["user"] = user
        if user=='test' and password=='test':
            return redirect(url_for("member"))
        else:
            return redirect(url_for("error"))
    else:
        if "user" in session:
            return redirect(url_for("member")) 
    
# 錯誤頁
@app.route("/error")
def error():
    return render_template('error.html')
    
# 會員頁
@app.route("/member")
def member():
    if "user" in session:
        user = session["user"]
        return render_template("member.html")
    else:
        return redirect('/')


# logout    
@app.route("/signout")
def logout():
    session.pop("user", None)
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)