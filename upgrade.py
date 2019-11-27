import sys
import requests
from ppadb.client import Client as AdbClient

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
#print(client.version())

APK_URL = 'https://tools.taskcluster.net/index/project.mobile.fenix.signed-nightly.nightly/latest'
#APK_PATH = "target.arm.apk"
#APK_PATH = "target.x86.apk"
APK_PATH = 'target.aarch64.apk'
MOZ_PACKAGE = 'org.mozilla.fenix'


# Default is "127.0.0.1" and 5037
devices = client.devices()
#device = client.device('emulator-5554')

def header(title):
    line = '-----------------------------------------'
    print('{0}\n{1}\n{0}'.format(line, title.upper()))


def apk_download():
    header('download')
    print('Beginning APK download: {0}\n\n'.format(MOZ_PACKAGE))
    r = requests.get(APK_URL)

def apk_install(device):
    header('INSTALL')
    print('installing {0} for device: {1}\n\n'.format(MOZ_PACKAGE, device.serial))
    device.install(APK_PATH)

# Check apk is installed
def apk_list(devices, device):
    header('LIST DEVICES')
    if len(devices) == 0:
        sys.exit('Error: no devices connected!')
    else:
        print('device: {0}'.format(device.serial))
        print('package installed: {0}'.format((device.is_installed(MOZ_PACKAGE))))
    print('\n\n')

def apk_uninstall(device):
    if device:
        header('UNINSTALL')
        print('uninstalling {0} for device: {1}'.format(MOZ_PACKAGE, device.serial))
        device.uninstall(MOZ_PACKAGE)
        print('\n\n')


if __name__ == '__main__':
    for device in devices:
        apk_download()
        apk_uninstall(device)
        #apk_list(devices, device)
        apk_install(device)
        apk_list(devices, device)
