import random
import string
import sys
import base64


def random_string():
    return '_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))


def new_guid(stream):
    return [
        stream[3] << 24 | stream[2] << 16 | stream[1] << 8 | stream[0],
        stream[5] << 8 | stream[4],
        stream[7] << 8 | stream[6],
        stream[8],
        stream[9],
        stream[10],
        stream[11],
        stream[12],
        stream[13],
        stream[14],
        stream[15],
    ]


def encode_object_guid(guid):
    guid = guid.replace('}', '').replace('{', '')
    guid_parts = guid.split('-')
    hex_string = (
        guid_parts[0][6:]
        + guid_parts[0][4:6]
        + guid_parts[0][2:4]
        + guid_parts[0][:2]
        + guid_parts[1][2:]
        + guid_parts[1][:2]
        + guid_parts[2][2:]
        + guid_parts[2][:2]
        + guid_parts[3]
        + guid_parts[4]
    )

    hex_array = bytearray.fromhex(hex_string)
    return base64.b64encode(hex_array)


def die():
    sys.exit()


def print_intro():

    print('    ___    ____  ___________                   ____')
    print('   /   |  / __ \/ ____/ ___/____  ____  ____  / __/')
    print('  / /| | / / / / /_   \__ \/ __ \/ __ \/ __ \/ /_  ')
    print(' / ___ |/ /_/ / __/  ___/ / /_/ / /_/ / /_/ / __/  ')
    print('/_/  |_/_____/_/    /____/ .___/\____/\____/_/     ')
    print('                        /_/                        \n')
    print('A tool to for AD FS security tokens')
    print('Created by @doughsec\n')
