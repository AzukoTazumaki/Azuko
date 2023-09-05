import os

directory = os.getcwd() + '/static/images'


def slider_albums():
    path = os.path.join(directory, 'carousel', 'carousel_albums')
    names = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.jpg'):
                names.append(
                    {
                        'cover': file,
                        'name': file.split('.')[0]
                    }
                )
    return names

