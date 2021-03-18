from flask import Flask, render_template,redirect,request,session,url_for

app = Flask(__name__)
app.secret_key = 'djdkillsdmck_kdkewdkwjs-dkskksaaxxls'

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/member')
    else:
        return render_template('index.html')

# 登入頁
@app.route('/signin', methods=["POST","GET"])
def signin():
    userId = request.form['userID']
    password = request.form['password']
    session['user'] = userId
    if userId == 'test' and password == 'test':
        return redirect('/member')
    else:
        session.pop("user",None)
        return redirect('/error')

# 會員頁
@app.route('/member')
def member():
    if 'user' in session:
        return render_template('member.html')
    else:
        return redirect('/')

# 錯誤頁
@app.route('/error')
def error():
    return render_template('error.html')

# 登出頁
@app.route('/signout')
def signout():
    session.pop('user',None)
    return redirect('/')


if __name__ == "__main__":
    app.run(port=3000)
