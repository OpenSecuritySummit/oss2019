import pandas as pd
from oss_hugo.API_Hugo_OSS import API_Hugo_OSS

class OSS_Schedule:
    def __init__(self):
        self.hugo = API_Hugo_OSS()

    def sessions_mapped_by_size(self):

        mapping = []
        for path, session in self.hugo.sessions().items():
            content    = session.get('content')
            metadata   = session.get('metadata')
            page_type  = metadata.get('type')
            title      = metadata.get('title')
            track      = metadata.get('track')
            organizers = metadata.get('organizers')
            participants = metadata.get('participants')
            if not organizers: organizers = []
            if not participants: participants = []
            if type(organizers) is str: organizers = organizers.split(',')
            if type(participants) is str: participants = participants.split(',')
            if 'TBD' in organizers: organizers.remove('TBD')
            if 'Pending' in organizers: organizers.remove('Pending')
            if 'you ?' in participants: participants.remove('you ?')

            if title and page_type:
                item = {
                    'title': title,
                    'track': track,
                    'page_type': page_type,
                    'organizers': organizers,
                    'participants': participants,
                    'content': len(content),
                    'path': path
                }
                mapping.append(item)

        df_mappings = pd.DataFrame(mapping)
        df_mappings = df_mappings[['title', 'track', 'page_type', 'content', 'organizers', 'participants']]
        df_sessions = df_mappings[df_mappings['page_type'] != 'track']
        df_sessions = df_sessions.sort_values(['content'], ascending=False).reset_index(drop=True)
        return df_sessions