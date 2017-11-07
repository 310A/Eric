from flask import Flask, url_for
app = Flask(__name__)

@app.route('/test/')
def hello_world():
    return 'Hello World!'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
with app.test_request_context():
    print url_for('hello_world')

if __name__ == '__main__':
    app.run(debug=True)