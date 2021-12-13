import subprocess


def install_apk(device, apk_path):
    command = f"adb -s {device} install {apk_path}"
    print(subprocess.getoutput(command))


def send_intent(device, action, data=""):
    if data:
        data = f' --es data "{data}"'
    command = f'adb -s {device} shell am broadcast -a {action}{data}'
    print(subprocess.getoutput(command))


def launch_app(device, package):
    command = f'adb -s {device} shell am start -n "{package}"/.MainActivity'
    print(subprocess.getoutput(command))
