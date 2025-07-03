import pyqrcode
youtube_url="https://www.google.com/search?q=python%20tutorials"
video_qr=pyqrcode.create(youtube_url)
video_qr.svg('video2.svg',scale=8)
