import json
import random
import subprocess

ACTION_DISCOVER = "com.example.devicerpc.action.DISCOVER"
ACTION_PAIR = "com.example.devicerpc.action.PAIR"
ACTION_UNPAIR = "com.example.devicerpc.action.UNPAIR"
ACTION_COMMAND = "com.example.devicerpc.action.COMMAND"


def install_apk(device, apk_path):
    command = f"adb -s {device} install {apk_path}"
    result = subprocess.getoutput(command)
    print(result)


def send_intent(device, action, data=""):
    if data:
        data = f' --es data "{data}"'
    command = f'adb -s {device} shell am broadcast -a {action}{data}'
    print(command)
    result = subprocess.getoutput(command)
    print(result)


def launch_app(device, package):
    command = f'adb -s {device} shell am start -n "{package}"/.MainActivity'
    result = subprocess.getoutput(command)
    print(result)


def send_rpc_command(device, method, params=""):
    command = {"jsonrpc": "2.0", "method": method, "params": params if params else "-", "id": str(random.randint(1, 1000))}
    command = encode_intent_data(command)
    send_intent(device, ACTION_COMMAND, command)


def encode_intent_data(message):
    payload = json.dumps(message)
    payload = f'{payload}'
    payload = payload.translate(str.maketrans({" ": r"\ ", "{": r"\{", "}": r"\}", "\\": r"\\", "'": r"\'", r'"': r'\"'}))
    print(payload)
    return payload
