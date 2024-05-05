from flask import Flask, render_template, request, redirect
from email.message import EmailMessage
import ssl
import smtplib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/send_email', methods=['GET', 'POST'])

def send_email():
    fname = request.form['fname']
    lname = request.form.get('lname')
    ename = request.form.get('ename')
    para = request.form.get('para')
    ctime = request.form.get('ctime')

    
    recipient_email = request.form['email']
    print(recipient_email,fname,lname,ename,ctime)
    sendmail(recipient_email,fname,lname,ename,ctime)
    redirect("/")
    return render_template("result.html", email=recipient_email,fname=fname,lname=lname,ename=ename,para=para,ctime=ctime)

def sendmail(recipient_email,fname,lname,ename,ctime):
    email_sender="projectfee2023group4@gmail.com"
    email_password= "vccw gzym tydk dywx"
    
    subject ="Regarding your Countdown page for event."
    body=f"{fname} {lname}, your {ename} countdown for {ctime} has been created .Thanks for using our platform for the work."
    
    em= EmailMessage()
    em['From']= email_sender
    em['To']=recipient_email
    em['subject']=subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        try:
          
            server.login(email_sender, email_password)

          
            server.sendmail(email_sender, recipient_email, em.as_string())
            print("Email sent successfully!")

        except Exception as e:
            print(f"Error: {e}")
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')