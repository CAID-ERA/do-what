# do-what
Deploy the flask app by:
```
cd Scripts
sudo sh ./init.sh
export FLASK_APP = app.py
cd ../Flask/
```
Run the web app without logging by:
```nohup python3 -m flask run -h 0.0.0.0 --port 80 >/dev/null 2>&1 &```

Or run the app in the debug mode by:
```python3 -m flask run -h 0.0.0.0 --port 80```

This app uses a remote MySQL database and it will be closed at around the end of Dec. 2018.
If there's any advice please email us at: iiivanzhu@gmail.com
