from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

notes = []

@app.route('/')
def home():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        note_text = request.form["note"]
        notes.append(note_text) 
        return redirect(url_for('home'))
    return render_template('add.html')

@app.route('/delete/<int:index>')
def delete_note(index):
    if 0 <= index < len(notes):
        del notes[index]
    return redirect(url_for('home'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_note(index):
    if 0 <= index < len(notes):
        if request.method == 'POST':
            notes[index] = request.form["note"]
            return redirect(url_for('home'))
        return render_template('edit.html', note=notes[index], index=index)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)