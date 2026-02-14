from flask import Flask, render_template, url_for, request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC

''''
This cretes the app which is runs on port 5000.
url_for used to generate urls dynamically.
Here sqllite used for learning with db name as test.db
'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db =SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0) 
    date_created = db.Column(db.DateTime, default=datetime.now(UTC))

    def __repr__(self):
        return f"<Task {self.id}>"

# @app.route('/')
# def index():
    ''''
    We can send the simple text here as a return will showed in front end
    '''
#     # return "Hello World"
    ''''
    This render_template option renders the html file
    '''
#     return render_template('index.html') 
''''
 1. Now instead of just delivering html file this route now allows POST method also.
'''
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an error adding data"
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)
    

''''
 1. Delete route takes the id as an parameter and does the DELETE operation
 2. Later redirected to the home page.
'''

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "Unable to delete the task"
    
''''
1. Update route takes the id as an parameter and does the UPDATE operation
2. Later redirects to the home page.
'''

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating task"

    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)