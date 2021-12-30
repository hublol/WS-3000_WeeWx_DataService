# installer for the WS-3000 driver
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return WS3000DSInstaller()

class WS3000DSInstaller(ExtensionInstaller):
    def __init__(self):
        super(WS3000DSInstaller, self).__init__(
            version="0.2",
            name='WS-3000 Data Service',
            description='Data Service for the WS-3000 station',
            author="hublol",
            author_email="hal.lol@tutanota.com",
            files=[('bin/user', ['bin/user/ws3000DataService.py'])]
            )