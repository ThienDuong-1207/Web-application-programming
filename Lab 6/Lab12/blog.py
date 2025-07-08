from flask import Flask, render_template, request

app = Flask(__name__)

# Tạo sample dictionary để lưu trữ bài viết
posts = {
    1: {"title": "First Post", "content": "This is the content of the first post."},
    2: {"title": "Second Post", "content": "This is the content of the second post."},
    3: {"title": "Third Post", "content": "This is the content of the third post."}
}

@app.route('/<int:post_id>')

def show_post(post_id):
    post = posts.get(post_id)
    if post:
        return render_template('blog.html', title=post['title'], content=post['content'])
    else:
        return "Post not found", 404
    
if __name__ == '__main__':
    app.run(debug=True) 