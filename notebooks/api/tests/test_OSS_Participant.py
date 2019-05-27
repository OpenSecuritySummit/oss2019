from unittest import TestCase

from pbx_gs_python_utils.utils.Dev import Dev

from oss_hugo.OSS_Participant import OSS_Participant


class test_OSS_Participant(TestCase):

    def setUp(self):
        self.oss_participant = OSS_Participant()
        self.result          = None
        self.test_name       = 'an test user'
        self.participant     =

    def tearDown(self):
        if self.result is not None:
            Dev.pprint(self.result)

    def test__init__(self):
        assert self.oss_participant.base_folder == 'content/participant'

