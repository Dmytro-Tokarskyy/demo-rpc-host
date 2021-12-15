import adb_shell as adb
import uiautomator2

# Smartphone
DEVICE_1_SERIAL = '420082fbc207251d'
DEVICE_1_MAC = '48:C7:96:D6:75:80'
# Tablet
DEVICE_2_SERIAL = '2d4250e40178cc0e'
DEVICE_2_MAC = '34:14:5F:AC:43:88'

PACKAGE = "com.example.devicerpc"

OK_BUTTON1 = "com.android.settings:id/button1"
OK_BUTTON2 = "android:id/button1"


def main():
    # Install apk to devices
    pass
    # Launch apk on devices
    adb.launch_app(DEVICE_1_SERIAL, PACKAGE)
    adb.launch_app(DEVICE_2_SERIAL, PACKAGE)

    # Send intent for discoverable to devices
    adb.send_rpc_command(DEVICE_1_SERIAL, "discover") # adb.send_intent(DEVICE_1_SERIAL, adb.ACTION_DISCOVER)
    device1_ui = uiautomator2.connect(DEVICE_1_SERIAL)
    device1_ui(resourceId=OK_BUTTON1).click()

    adb.send_rpc_command(DEVICE_2_SERIAL, "discover")
    device2_ui = uiautomator2.connect(DEVICE_2_SERIAL)
    device2_ui(resourceId=OK_BUTTON2).click()

    # From device 1 send pair request to device 2
    adb.send_rpc_command(DEVICE_1_SERIAL, "pair", f'"{DEVICE_2_MAC}"') #adb.send_intent(DEVICE_1_SERIAL, adb.ACTION_PAIR, DEVICE_2_MAC)

    # # Accept pairing on devices
    device1_ui(resourceId=OK_BUTTON1).click()
    device2_ui(resourceId=OK_BUTTON2).click()

    adb.send_rpc_command(DEVICE_1_SERIAL, "unpair", f'"{DEVICE_2_MAC}"') #adb.send_intent(DEVICE_1_SERIAL, adb.ACTION_UNPAIR, DEVICE_2_MAC)
    adb.send_rpc_command(DEVICE_2_SERIAL, "unpair", f'"{DEVICE_2_MAC}"') #adb.send_intent(DEVICE_2_SERIAL, adb.ACTION_UNPAIR, DEVICE_1_MAC)


if __name__ == '__main__':
    main()
