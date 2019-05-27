from oss_hugo.Hugo_Page import Hugo_Page


class OSS_Participant(Hugo_Page):

    def __init__(self):
            super().__init__(base_folder='content/participant')
        self.data = None

    def load(self,path):
        self.data = super().load(path)

    def save(self):
        super().save(self.data)
