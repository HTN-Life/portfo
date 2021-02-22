from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:pagename>')
def htmlpage(pagename):
    return render_template(pagename)

def addtodb(data):
	with open('database.txt', mode = 'a') as database:
		email = data['Email']
		subject = data['Subject']
		message = data['Message']
		file = database.write(f'Email = {email},\nSubject = {subject},\nMessage = {message}\n\n')

def addtocsvdb(data):
	with open('database.csv', mode = 'a',newline ='') as database2:
		email = data["Email"]
		subject = data["Subject"]
		message = data["Message"]
		csv_writer =csv.writer(database2, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method=='POST':
		try:
			data = request.form.to_dict()
			addtocsvdb(data)
			addtodb(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not save to DB'
	else :
		return 'something went wrong. Try Again!'

