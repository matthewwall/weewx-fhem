# installer for FHEM report

from setup import ExtensionInstaller

def loader():
    return FHEMInstaller()

class FHEMInstaller(ExtensionInstaller):
    def __init__(self):
        super(FHEMInstaller, self).__init__(
            version="0.1",
            name='fhem',
            description='report that emits data in FHEM format',
            author="Hans (Luc) Heijst",
            config={
                'StdReport': {
                    'fhem': {
                        'skin':'fhem',
                        'HTML_ROOT':'fhem'}}},
            files=[('skins/fhem', ['skins/fhem/fhem.txt.tmpl'])]
            )
