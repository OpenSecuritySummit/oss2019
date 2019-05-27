import pandas as pd
import qgrid
from pbx_gs_python_utils.utils.Files import Files
from oss_hugo.Files_Utils import Files_Utils

from oss_hugo.Hugo_Page import Hugo_Page
from oss_hugo.OSS_GSheet_Data import OSS_GSheet_Data
from oss_hugo.OSS_Participant import OSS_Participant


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
    def participants(self,reload=True):
        if self._participants is None or reload:
            self._participants = self.load_files(self.md_files_participants())
        return self._participants

    def participants_metadatas(self):
        #return self.participants()
        return [participant.get('metadata') for participant in self.participants().values()]

    def gsheet_data(self):
        return OSS_GSheet_Data()

    def df_merged_gsheet_and_hugo_data(self,reload=False):
        df_hugo = pd.DataFrame(self.participants_metadatas())
        df_gsheet = self.gsheet_data().df_participants_onsite(reload)
        df_gsheet['GSheet'] = True
        df_hugo  ['Hugo'  ] = True
        df_hugo  ['Name'  ] = df_hugo['title']
        df_hugo = df_hugo[['Name', 'status', 'company', 'Hugo']]
        df_both = pd.merge(df_hugo, df_gsheet, on='Name', how='outer').fillna('')
        #df_both.fillna('*')
        df_both = df_both[['Name', 'company', 'Company', 'Payment Status', 'GSheet', 'Hugo']]
        df_both = df_both[df_both['Name'] != '']
        return df_both

    def qgrid_merged_gsheet_and_hugo_data(self,reload=False):
        df_both = self.df_merged_gsheet_and_hugo_data(reload)
        return qgrid.show_grid(df_both)