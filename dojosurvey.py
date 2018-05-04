from flask import Flask, render_template, request, redirect
app= Flask(__name__)
@app.route('/')
def index():
	return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
	print("Got Post Info")
	print (request.form)
	name=request.form['name']
	dojo=request.form['dojo']
	lang=request.form['lang']

	return render_template('submit.html', name=name, lang=lang, dojo=dojo)
@app.route('/danger')
def danger():
	print("a user tried to visit /danger. we have redirected the user to /")
	return redirect('/')
if __name__=="__main__":
	app.run(debug=True)