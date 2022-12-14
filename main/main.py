from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from producer import publish
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class Blog(db.Model):
    id: int
    title: str
    description: str
    image: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    image = db.Column(db.String(200))



@app.route('/api/blogs')
def index():
    return jsonify(Blog.query.all())

@app.route('/api/blog/<int:id>/view',methods=['POST'])
def view(id):
    publish('blog_view', id)
    return jsonify(Blog.query.filter_by(id=id).first())


@app.route('/api/blog/<int:id>/like', methods=['POST'])
def like(id):
    publish('blog_liked', id)
    return jsonify({
        'message': 'success'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')