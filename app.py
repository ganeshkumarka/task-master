# from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# from flask_migrate import Migrate


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     category = db.Column(db.String(50), nullable=False)
#     due_date = db.Column(db.Date, nullable=True)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     status = db.Column(db.String(20), default='Pending')

# @app.route('/')
# def index():
#     tasks = Task.query.order_by(Task.date_created.desc()).all()
#     return render_template('index.html', tasks=tasks)

# @app.route('/add_task', methods=['POST'])
# def add_task():
#     content = request.form['content']
#     category = request.form['category']
#     due_date_str = request.form['due_date']
#     due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
    
#     new_task = Task(content=content, category=category, due_date=due_date)
    
#     try:
#         db.session.add(new_task)
#         db.session.commit()
#         return redirect(url_for('index'))
#     except:
#         return 'There was an issue adding your task'

# @app.route('/delete_task/<int:id>')
# def delete_task(id):
#     task_to_delete = Task.query.get_or_404(id)
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect(url_for('index'))
#     except:
#         return 'There was a problem deleting that task'

# @app.route('/update_task/<int:id>', methods=['POST'])
# def update_task(id):
#     task = Task.query.get_or_404(id)
#     task.content = request.form['content']
#     task.category = request.form['category']
#     task.status = request.form['status']
#     due_date_str = request.form['due_date']
#     task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
    
#     try:
#         db.session.commit()
#         return redirect(url_for('index'))
#     except:
#         return 'There was an issue updating your task'

# @app.route('/get_task/<int:id>')
# def get_task(id):
#     task = Task.query.get_or_404(id)
#     return jsonify({
#         'id': task.id,
#         'content': task.content,
#         'category': task.category,
#         'due_date': task.due_date.isoformat() if task.due_date else None,
#         'status': task.status
#     })

# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.Date, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.date_created.desc()).all()
    print(f"Number of tasks: {len(tasks)}")  # Debugging line
    for task in tasks:
        print(f"Task ID: {task.id}, Content: {task.content}")  # Debugging line
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    content = request.form['content']
    category = request.form['category']
    due_date_str = request.form['due_date']
    due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
    
    new_task = Task(content=content, category=category, due_date=due_date)
    
    try:
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue adding your task'

@app.route('/delete_task/<int:id>')
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was a problem deleting that task'

@app.route('/update_task/<int:id>', methods=['POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    task.content = request.form['content']
    task.category = request.form['category']
    task.status = request.form['status']
    due_date_str = request.form['due_date']
    task.due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None
    
    try:
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue updating your task'

@app.route('/get_task/<int:id>')
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({
        'id': task.id,
        'content': task.content,
        'category': task.category,
        'due_date': task.due_date.isoformat() if task.due_date else None,
        'status': task.status
    })

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)