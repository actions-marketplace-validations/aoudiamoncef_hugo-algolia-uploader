import os
import json

from algoliasearch.search_client import SearchClient

client = SearchClient.create(os.environ.get("INPUT_APP_ID"), os.environ.get("INPUT_ADMIN_KEY"))
index_name = os.environ.get("INPUT_INDEX_NAME")
index_name_separator = os.environ.get("INPUT_INDEX_NAME_SEPARATOR")
index_file_directory = os.environ.get("INPUT_INDEX_FILE_DIRECTORY")
index_file_name = os.environ.get("INPUT_INDEX_FILE_NAME")
languages = os.environ.get("INPUT_INDEX_LANGUAGES").split(",")
github_workspace = os.environ.get("GITHUB_WORKSPACE")


def upload(path, index):
    if os.path.isfile(path):
        with open(path) as f:
            records = json.load(f)
            index.save_objects(records, {'autoGenerateObjectIDIfNotExist': True})


upload("{}/{}/{}".format(github_workspace, index_file_directory, index_file_name), client.init_index(index_name))

for language in languages:
    i18n_index = client.init_index("{}{}{}".format(index_name, index_name_separator, language))
    upload("{}/{}/{}/{}".format(github_workspace, index_file_directory, language.lower(), index_file_name), i18n_index)
