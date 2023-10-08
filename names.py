import os
from typing import Union


class ProjectNames:
    def __init__(self, path_covers: str):
        self.path_covers_default = path_covers
        self.directory = os.getcwd() + '/static/images/projects/'
        self.path_covers = os.path.join(self.directory, self.path_covers_default)
        self.keys = ['cover', 'name', 'button', 'url', 'artist']
        self.image_expansions = ['.jpg', '.png']

    def make_project_info(self, key_1: str, key_2: str, key_3: str, image_expansion: str) -> list:
        project_info: list = []
        for root, dirs, files in os.walk(self.path_covers):
            for file in files:
                if file.endswith(image_expansion):
                    if key_3 is None:
                        project_info.append({key_1: file, key_2: file.split('.')[0]})
                    else:
                        project_info.append({
                            key_1: file,
                            key_2: file.split('.')[0].split('|')[1],
                            key_3: file.split('.')[0].split('|')[0]
                        })
        sorted_project_info: list = sorted(project_info, key=lambda x: x[key_1], reverse=True)
        return sorted_project_info

    def get_album_info(self):
        covers_and_names: list = self.make_project_info(self.keys[0], self.keys[1], None, self.image_expansions[0])
        buttons_and_urls: list = self.make_project_info(self.keys[2], self.keys[3], None, self.image_expansions[1])
        for index, item_dict in enumerate(buttons_and_urls):
            covers_and_names[index][self.keys[2]] = item_dict[self.keys[2]]
            covers_and_names[index][self.keys[3]] = item_dict[self.keys[3]]
        return covers_and_names

    def get_single_or_featuring_info(self):
        covers_and_names: list = self.make_project_info(self.keys[0], self.keys[1], self.keys[4], self.image_expansions[0])
        return covers_and_names


a = ProjectNames('singles')
print(a.get_single_or_featuring_info())
