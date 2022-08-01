from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pandas as pd
import reader

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        try:
            data = reader.init_db()
            reader.compile(data,['/Users/mickflannery/Downloads/lmao/20-34-413-063-0000.pdf', '/Users/mickflannery/Downloads/lmao/20-34-413-064-0000.pdf', '/Users/mickflannery/Downloads/lmao/20-34-413-065-0000.pdf', '/Users/mickflannery/Downloads/lmao/20-34-413-066-0000.pdf', 
            '/Users/mickflannery/Downloads/lmao/X - 20-34-413-046-0000.pdf', '/Users/mickflannery/Downloads/lmao/X - 20-34-413-061-000.pdf', 
            '/Users/mickflannery/Downloads/lmao/X - 20-34-413-062-0000.pdf']).to_csv("test.csv") # Testing!!!!
            return redirect('/')
        except:
            return "There was an error"
        # task_content = request.form['content']#input id
        # new_task = Todo(content=task_content)

        # try:
        #     db.session.add(new_task)
        #     db.session.commit()
        #     return redirect('/')
        # except:
        #     return "There was an issue adding task"
    elif len(pd.read_csv("test.csv")) == 0:
        data = reader.init_db()
        data.to_csv("test.csv")
        return render_template('index.html',  tables=[data.to_html(classes='data', header="true")])
    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        data = pd.read_csv("test.csv")
        return render_template('index.html',  tables=[data.to_html(classes='data', header="true")])

# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Todo.query.get_or_404(id)
#     try:
#         db.session.delete(task_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return "Problem with deleting"

# @app.route('/update/<int:id>', methods=['GET','POST'])
# def update(id):
#     task = Todo.query.get_or_404(id)
#     if request.method == 'POST':
#         task.content = request.form['content']
#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "Error updating info"
#     else:
#         return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)