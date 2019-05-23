import pandas as pd
from pbx_gs_python_utils.utils.Files import Files
from pbx_gs_python_utils.utils.Json import Json


class OSS_GSheet_Data:
    def __init__(self):
        self.data_folder = Files.path_combine(__file__, '../../../../data/_sync/json')

    def data_participants_onsite(self):
        data = Json.load_json(Files.path_combine(self.data_folder, 'participants_onsite.json'))
        return list(data.values())

    def data_participants_remote(self):
        data = Json.load_json(Files.path_combine(self.data_folder, 'participants_remote.json'))
        return list(data.values())

    def df_participants_onsite(self):
        df = pd.DataFrame(self.data_participants_onsite())
        return df

    def df_participants_remote(self):
        df = pd.DataFrame(self.data_participants_remote())
        return df