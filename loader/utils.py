def save_picture(picture):
    """ функция сохранения файла в папаку uploads"""
    filename = picture.filename
    path = f"./uploads/images/{filename}"
    picture.save(path)
    return path