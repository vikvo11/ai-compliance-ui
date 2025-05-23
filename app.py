from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

scripts = []  # List to store JS URLs

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('script_url')
        if url:
            scripts.append(url)
        return redirect(url_for('index'))
    return render_template('index.html', scripts=scripts)

@app.route('/delete/<int:script_id>', methods=['POST'])
def delete_script(script_id):
    if 0 <= script_id < len(scripts):
        scripts.pop(script_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
