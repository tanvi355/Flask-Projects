from flask import Flask, render_template, request

#declare the app
app = Flask(__name__)

#start an app route
@app.route('/')

#declare the main function
def main():
    return render_template('index.html')

#form submission route
@app.route('/send', methods=['POST'])
def send():
    try:
        if request.method == 'POST':
            #start pulling the data (name) from form input
            var1 = request.form['var1']
            var2 = request.form['var2']

            #calculating answer
            if request.form.get('add'):
                ans = float(var1) + float(var2)
            elif request.form.get('subtract'):
                ans = float(var1) - float(var2)
            elif request.form.get('multiply'):
                ans = float(var1) * float(var2)
            else:
                ans = float(var1) / float(var2)
            return render_template('index.html', result=ans)
    except ValueError as error:
        error = "Please enter all the input fields."
        return render_template('index.html', result=error)

if __name__ == '__main__':
    app.run(debug=True)
