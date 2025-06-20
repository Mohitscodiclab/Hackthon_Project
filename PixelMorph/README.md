# 🖼️ PixelMorph

A modern web-based tool to convert images into JPG, PNG, SVG, PDF, or DOCX using Flask. Designed with a clean UI, responsive layout, and smooth user experience.
## Python

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)

## Flask

![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)

## Licence

![License](https://img.shields.io/badge/License-MIT-yellow.svg)


---

## ✨ Features

* ✅ Convert images to **JPG, PNG, SVG, PDF, and DOCX**
* 🖱️ Drag & drop file upload with live preview
* 📱 Mobile-first responsive design
* 🎨 Clean glassmorphism UI
* ♻️ Auto-deletes old temporary files
* 🔐 Secure file upload and format validation

---

## 🚀 Getting Started

### Requirements

* Python 3.7+
* `pip` (Python package manager)

### Setup
To let another user run **PixelMorph** (your Flask-based image converter) on their own PC, you can guide them with these **clear and simple steps**.

---

## 🧑‍💻 How Another User Can Use PixelMorph on Their PC

### ✅ 1. **Install Prerequisites**

Make sure Python is installed:

* Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)
* During installation, **check the box** that says **"Add Python to PATH"**

### 🧾 2. **Download the Project**

There are two ways:

#### Option A: Clone via Git

```bash
https://github.com/Mohitscodiclab/Hackthon_Project.git
cd PixelMorph
```

#### Option B: Download ZIP

1. Visit: [https://github.com/mohitscodiclab/Hackathon/PixelMorph](https://github.com/Mohitscodiclab/Hackthon_Project/tree/main/PixelMorph)
2. Find the `PixelMorph` folder
3. Click **Code → Download ZIP**
4. Extract it and open the folder in terminal

---

### 🏗️ 3. **Set Up the Environment**

Open a terminal or command prompt inside the project folder.

#### Create Virtual Environment

```bash
pip install -r requirements.txt
```

> If there’s no `requirements.txt`, run:

```bash
pip install Flask Pillow reportlab python-docx svgwrite Werkzeug
```

---

### ▶️ 5. **Run the App**

```bash
python app.py
```

> The terminal will show something like:

```
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
```

---

### 🌐 6. **Use in Browser**

Open your browser and go to:

```
http://localhost:8000
```

Now they can upload images and convert them into JPG, PNG, SVG, PDF, or DOCX with a clean UI.

---

## 📝 Optional: Make It Even Easier

If you want to make it beginner-friendly:

1. Add a `run.bat` (Windows) or `run.sh` (Mac/Linux) file to automate setup
2. Bundle a `README.txt` with these instructions
3. Host the ZIP on GitHub Releases or Google Drive with a friendly name like `PixelMorph_Installer.zip`


---

## 📦 Dependencies

Just copy and paste the command in your terminal or powershell and download al the dependencies:

```
pip install Flask Pillow reportlab python-docx svgwrite Werkzeug

```

---

## 🏗️ Folder Structure

```
pixelmorph/
│
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # Frontend HTML
├── uploads/             # Temp uploaded images
├── outputs/             # Converted output files
└── README.md            # Project documentation
```

---

## 🧩 Supported Formats

| Input     | Output Format | Notes                               |
| --------- | ------------- | ----------------------------------- |
| Any image | JPG           | Converts transparency to white      |
|           | PNG           | Lossless, retains transparency      |
|           | SVG           | Encodes as Base64 inside SVG        |
|           | PDF           | Scaled and centered on A4 page      |
|           | DOCX          | Embedded as an image in a Word file |


---

## 📡 API Endpoints

* `POST /upload` – Upload an image
* `POST /convert` – Convert image (`{ filename, format }`)
* `GET /download/<filename>` – Download converted file
* `GET /cleanup` – Delete files older than 1 hour

---

## ⚙️ Configuration Tips

* **Max upload size**
  Set this to prevent large file abuse:

  ```python
  app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
  ```

* **Secret key**
  Replace with your own in production:

  ```python
  app.secret_key = 'your-production-secret-key'
  ```

* **Production deployment**
  Use with Gunicorn or similar WSGI server:

  ```bash
  export FLASK_ENV=production
  export SECRET_KEY=your-production-secret
  ```

---

## 🧹 Auto Cleanup

To keep storage clean, old files can be removed automatically. Add this to crontab for hourly cleanup:

```bash
0 * * * * curl http://localhost:8000/cleanup
```
---

## 🤝 Contributing

1. Fork this repo
2. Create a new branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push your branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

* [Flask](https://flask.palletsprojects.com/)
* [Pillow](https://python-pillow.org/)
* [ReportLab](https://www.reportlab.com/)
* [python-docx](https://python-docx.readthedocs.io/)
* [SVGWrite](https://pypi.org/project/svgwrite/)
* [Font Awesome](https://fontawesome.com) – For UI icons

> Built with ❤️ by [@Mohitscodiclab](https://github.com/mohitscodiclab)

