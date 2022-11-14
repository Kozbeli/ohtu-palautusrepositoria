from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print("content")
        print(content)

        # tiedoston sisältö sanakirjana
        data = toml.loads(content)
        print("data")
        print(data)
        
        parsed_data = data['tool']['poetry']
        print("parsed_data")
        print(parsed_data)

        name = parsed_data['name']
        print("name")
        print(name)

        description = parsed_data['description']
        print("description")
        print(description)

        dependencies = parsed_data['dependencies']
        print("dependencies")
        print(dependencies)

        dev_dependencies = parsed_data['dev-dependencies']
        print("dev_dependencies")
        print(dev_dependencies)


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies)
