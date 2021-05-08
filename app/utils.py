import os
from werkzeug.utils import secure_filename
from config import BASEDIR


def load_media(data):
    media_folder = os.path.join(BASEDIR, 'media')

    filename = secure_filename(data.filename)
    print(filename)
    file_type = filename.split('.')[-1]
    if file_type in ["jpg", "png"]:
        media_folder = os.path.join(media_folder, "images")
    print(f"Loading file {os.path.join(media_folder, filename)}")
    data.save(os.path.join(media_folder, filename))
    return os.path.join(media_folder, filename)
    
    
    