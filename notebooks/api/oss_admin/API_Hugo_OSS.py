from pbx_gs_python_utils.utils.Files import Files
from oss_admin.Files_Utils import Files_Utils

from oss_admin.Hugo_Page import Hugo_Page
from oss_admin.OSS_Participant import OSS_Participant


class API_Hugo_OSS:

    def __init__(self):
        self.folder_oss = Hugo_Page().folder_oss
        self._participants = None

    def md_files_in_folder(self, target):
       path = Files.path_combine(self.folder_oss, target)
       return Files_Utils.all_files_recursive_with_extension(path,'.md')

    def md_files_participants(self):
        return self.md_files_in_folder(OSS_Participant().base_folder)


    def load_files(self,paths):
        results = {}
        for path in paths:
            data = Hugo_Page().load(path)
            if data:
                results[data.get('path')] = data
        return results

    #def save_file(self, data):
    #@use_local_cache_if_available
    def participants(self,reload=False):
        if self._participants is None or reload:
            self._participants = self.load_files(self.md_files_participants())
        return self._participants

    def participants_metadatas(self):
        #return self.participants()
        return [participant.get('metadata') for participant in self.participants().values()]
