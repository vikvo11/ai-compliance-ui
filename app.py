from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# In-memory list to store scripts with optional attributes
scripts = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('script_url')
        backend = request.form.get('backend')
        stream = request.form.get('stream') or 'true'
        key = request.form.get('key') or 'MY_PARTNER_KEY'
        allowed_origin = request.form.get('allowed_origin') or 'https://client.com'
        defer = bool(request.form.get('defer'))

        if url:
            scripts.append({
                'src': url,
                'backend': backend,
                'stream': stream,
                'key': key,
                'allowed_origin': allowed_origin,
                'defer': defer
            })

        return redirect(url_for('index'))
    return render_template('index.html', scripts=scripts)

@app.route('/delete/<int:script_id>', methods=['POST'])
def delete_script(script_id):
    if 0 <= script_id < len(scripts):
        scripts.pop(script_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
