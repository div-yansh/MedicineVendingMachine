from flask import Flask, request, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES
from prescription import prescription

app = Flask(__name__)
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "img"
configure_uploads(app, photos)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=["POST"])
def getvalue():
	name = request.form["name"]
	image = request.files["image"]
	photos.save(image)
	medicine, price, total = prescription()
	return render_template("response.html", name=name, medicine=medicine, price=price, total=total)

if __name__ == "__main__":
	app.run(debug=True)