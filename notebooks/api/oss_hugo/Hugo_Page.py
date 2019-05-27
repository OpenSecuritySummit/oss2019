import frontmatter
from pbx_gs_python_utils.utils.Files import Files

class Hugo_Page():
    def __init__(self, base_folder=None):
        self.folder_oss    = Files.path_combine(__file__, '../../../..')
        self.base_folder   = base_folder
        self.file_template = Files.path_combine(self.folder_oss,"{0}/{1}".format(self.base_folder,'_template.md'))


    def create(self, name):
        template = self.load(self.file_template)
        template['metadata']['title'] = name
        template['path']  = template['path'].replace('_template', self.fix_name(name))
        file_path = self.md_file_path(template['path'])
        if Files.exists(file_path):
            return { 'status': 'error', 'data':'target file already existed: {0}'.format(file_path)}
        return self.save(template)

    def delete(self, name):
        virtual_path = "{0}/{1}".format(self.base_folder, self.fix_name(name) + '.md')
        full_path = self.md_file_path(virtual_path)
        if Files.exists(full_path) is False:
            return False
        Files.delete(full_path)

        return Files.exists(full_path) is False

    def fix_name(self, name):
        return name.replace(' ','-').lower()

    def md_file_path(self, virtual_path:str):
        if virtual_path.startswith('/'): virtual_path = virtual_path[1:]
        return Files.path_combine(self.folder_oss,virtual_path)

    def load(self, path):
        if Files.exists(path):
            file_data     = frontmatter.load(path)
            relative_path = path.replace(self.folder_oss,'')
            data = { 'path': relative_path , 'content': file_data.content, 'metadata': file_data.metadata }
            return data

    def save(self, data):
        try:
            post              = frontmatter.Post(data.get('content'))
            post.metadata     = data.get('metadata')
            for key, value in post.metadata.items():
                default_value = '' if key not in ['sessions'] else []
                post.metadata[key] = value if value else default_value

            file_path = self.md_file_path(data['path'] )

            Files.write(file_path, frontmatter.dumps(post))
            if Files.exists(file_path):
                return { 'status': 'ok', 'data': data}
            else:
                return {'status': 'error', 'data': 'file not saved ok: {0}'.format(file_path) }
        except Exception as error:
            return { 'status': 'error', 'data': error }