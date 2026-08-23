from python:3.11
workdir /app
copy requirements.txt
run pip install -r requirements.txt
copy app.py .
expose 5000
cmd ["python", "app.py"]
