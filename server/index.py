# Import thư viện chuẩn

# Import thư viện bên ngoài
from flask import Flask, render_template

# Import module, package trong project
from boitoan.route import boi_toan

app = Flask(__name__,
            static_folder="../client/static",
            template_folder="../client/template")

# Register blueprint
app.register_blueprint(boi_toan)


# デフォルトのルート
@app.route('/', defaults={'path': ''})
# その他のルート
@app.route('/<path:path>')
def main(path):
    return render_template('index.html')


if __name__ == "__main__":
    # アプリ開始
    app.run(host="127.0.0.1", port=5000, debug=True)
