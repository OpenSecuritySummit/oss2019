from pbx_gs_python_utils.utils.Files import Files

from oss_hugo.Files_Utils import Files_Utils
from oss_hugo.Hugo_Page import Hugo_Page


class OSS_Participant:

    def __init__(self, name=None, folder_oss=None):
        self.base_folder  = 'content/participant/'
        self.hugo_page    = Hugo_Page(base_folder=self.base_folder,folder_oss=folder_oss)
        self.name         = name.strip() if name else None
        self.data         = None
        self.path_md_file = None
        if self.name:
            self.load()

    def create(self):
        if self.exists() is False:
            self.hugo_page.create(self.name)
            self.load()
        return self

    def delete(self):
        if self.exists() is False:
            return False
        self.hugo_page.delete(self.path_md_file)
        return self.exists() is False

    def delete_field(self,field, auto_save=False):
        if field in self.fields():
            del self.metadata()[field]
            if auto_save:
                self.save()
            return True
        return False

    def exists(self):
        self.load()
        return Files.exists(self.path_md_file)

    def field(self, key, value=None):
        metadata = self.metadata()
        if metadata:
            if value is not None:
                metadata[key] = value
                return self
            else:
                return metadata.get(key)
        return None

    def fields(self):
        metadata = self.metadata()
        if metadata:
            return list(set(self.metadata()))
        return []

    def load(self,reload=False):
        if self.data is None or reload:
            path = self.name
            if Files.exists(path) and '.md' in path:
                self.path_md_file = path
            else:
                if '.md' not in path:
                    path = self.hugo_page.fix_name(path) + '.md'
                if self.name.startswith(self.base_folder) is False:     # fix path
                    path = self.base_folder + path
                self.path_md_file = self.hugo_page.md_file_path(path)
            if Files.not_exists(self.path_md_file):
                self.path_md_file = self.hugo_page.find_in_md_files(self.name)
            self.data = self.hugo_page.load(self.path_md_file)
            title = self.field('title')
            if title:
                self.name = title
        return self

    def metadata(self):
        if self.data:
            return self.data.get('metadata')
        return None

    def save(self):
        self.hugo_page.save(self.data)
        return self

    def set_field(self,key, value):
        return self.field(key,value)