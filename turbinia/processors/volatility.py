# -*- coding: utf-8 -*-
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Evidence processor for raw memory resources."""

from __future__ import unicode_literals

import logging
import re
import subprocess

from turbinia import TurbiniaException

log = logging.getLogger('turbinia')

def PreprocessProfile(local_path):
    """Executes volatility to determine the appropiate profile"""

    return 'WinXPSP2x86'
    """
    # TODO: Make this configurable depending on install
    vol_cmd = ['python2', '/bin/vol', '-f', local_path, 'imageinfo']
    log.info('Running command {0:s}'.format(' '.join(vol_cmd)))
    try:
        proc = subprocess.check_output(vol_cmd)
    except subprocess.CalledProcessError as e:
        raise TurbiniaException('Failed to identify rawmemory profile {0!s}'
            .format(e))

    # TODO: Update this regex to be less disgusting!
    vol_re = re.match('.*\ (.*),.*', proc.decode("utf-8"))
    # Check we have at least 1 match and pull out first match
    if len(vol_re.groups()) >= 1:
        profile = vol_re.group(1)
        log.info('Found profile {0:s} using imageinfo'.format(profile))
    else:
        log.warning('Unable to determine profile using imageinfo')

    profile = 'WinXPSP2x86'
    return profile
    """

def PreprocessModules(self):
    # Mac profiles (^mac_\S*)
    """
    if self.profile.startswith('Mac'):
        vol_cmd = ['python2', '/bin/vol', '--info']
        vol_out = subprocess.check_output(vol_cmd)
        # Find all command prepended with mac_
        modules = re.findall('(mac_\S*)', vol_out.decode('utf-8'))
        modules = ' '.join(modules)
    # Windows profiles
    elif self.profile.startswith(('Win', 'Vista')):
        modules = 'pslist'
    return modules
    """
