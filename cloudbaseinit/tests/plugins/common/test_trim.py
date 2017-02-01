# Copyright 2013 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import unittest

try:
    import unittest.mock as mock
except ImportError:
    import mock

from cloudbaseinit.plugins.common import base
from cloudbaseinit.plugins.common import trim
from cloudbaseinit.tests import testutils


class TrimPluginPluginTests(unittest.TestCase):

    def setUp(self):
        self._trim_plugin = trim.TrimConfigPlugin()

    @testutils.ConfPatcher('trim_enabled', True)
    @mock.patch('cloudbaseinit.osutils.factory.get_os_utils')
    def test_trim_enable(self, mock_get_os_utils):
        shared_data = 'fake_shared_data'
        mock_os_utils = mock.MagicMock()
        mock_get_os_utils.return_value = mock_os_utils

        response = self._trim_plugin.execute(None, shared_data)
        mock_os_utils.enable_trim.assert_called_once_with(True)

        self.assertEqual(response, (base.PLUGIN_EXECUTION_DONE, False))

    @testutils.ConfPatcher('trim_enabled', False)
    @mock.patch('cloudbaseinit.osutils.factory.get_os_utils')
    def test_trim_disable(self, mock_get_os_utils):
        shared_data = 'fake_shared_data'
        mock_os_utils = mock.MagicMock()
        mock_get_os_utils.return_value = mock_os_utils

        response = self._trim_plugin.execute(None, shared_data)
        mock_os_utils.enable_trim.assert_called_once_with(False)

        self.assertEqual(response, (base.PLUGIN_EXECUTION_DONE, False))

    def test_get_os_requirements(self):
        response = self._trim_plugin.get_os_requirements()

        self.assertEqual(response, ('win32', (6, 1)))
