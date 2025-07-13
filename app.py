from flask import Flask, render_template, request, redirect, url_for
from utils.db import db
from models.blog import Blog, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    blogs = Blog.query.all()
    return render_template('blog.html', blogs=blogs)

@app.route('/add-blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        name = request.form['name']
        email = request.form['email']
        country = request.form['country']
        gender = request.form['gender']

        author = Author.query.filter_by(email=email).first()
        if not author:
            author = Author(name=name, email=email, country=country, gender=gender)
            db.session.add(author)
            db.session.commit()

        blog = Blog(title=title, content=content, author_id=author.author_id)
        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('blog'))

    return render_template('add_blog.html')

@app.route('/delete-blog/<int:blog_id>', methods=['POST'])
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    if blog:
        db.session.delete(blog)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
