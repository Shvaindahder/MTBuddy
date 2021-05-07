import os
from werkzeug.utils import secure_filename


def load_media(data):
    media_folder = get_config_variable("MEDIAFILES_FOLDER")
    if media_folder is None:
        media_folder = os.path.abspath("../media")

    filename = secure_filename(data.filename)
    file_type = filename.split['.'][-1]
    if file_type in ["jpg", "png"]:
        media_folder = os.path.join(media_folder, "img")

    data.save(os.path.join(media_folder, filename))
    
    
    