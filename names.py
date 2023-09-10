import os


class ProjectNames:
    def __init__(self, path_covers: str):
        self.directory = os.getcwd() + '/static/images/carousel'
        self.path_covers = os.path.join(self.directory, path_covers)
        self.keys = ['cover', 'name', 'button', 'url']
        self.image_expansions = ['.jpg', '.png']

    def make_project_info(self, key_1: str, key_2: str, image_expansion: str) -> list:
        project_info: list = []
        for root, dirs, files in os.walk(self.path_covers):
            for file in files:
                if file.endswith(image_expansion):
                    project_info.append(
                        {
                            key_1: file,
                            key_2: file.split('.')[0]
                        }
                    )
        sorted_project_info: list = sorted(project_info, key=lambda x: x[key_1], reverse=True)
        return sorted_project_info

    def get_project_info(self):
        covers_and_names: list = self.make_project_info(self.keys[0], self.keys[1], self.image_expansions[0])
        buttons_and_urls: list = self.make_project_info(self.keys[2], self.keys[3], self.image_expansions[1])
        for index, item_dict in enumerate(buttons_and_urls):
            covers_and_names[index][self.keys[2]] = item_dict[self.keys[2]]
            covers_and_names[index][self.keys[3]] = item_dict[self.keys[3]]
        return covers_and_names

