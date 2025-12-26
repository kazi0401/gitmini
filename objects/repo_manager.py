

'''
Docstring for objects.repo_manager

Repo manager should contain the information needed
to handle everything meta-data related. 
'''
import os

class RepoManager:
    METADATA_FOLDER = '_gitmini'

    def __init__(self):
       self._create_folder()

    def _create_folder(self):
        try:
            os.mkdir(RepoManager.METADATA_FOLDER)
            print(f"'{RepoManager.METADATA_FOLDER}' initalized successfully.")
        except FileExistsError:
            print(f"'{RepoManager.METADATA_FOLDER}' already initialized.")
        except PermissionError:
            print(f"Permission denied: Unable to create '{RepoManager.METADATA_FOLDER}'.")
        except Exception as e:
            print(f"An error occurred: {e}")


