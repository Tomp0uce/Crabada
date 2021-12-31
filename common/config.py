from .dotenv import getenv
import os

# Project directory
rootDir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Teams
teams = [
    {
        'id': getenv('USER_1_TEAM_1'),
        'userAddress': getenv('USER_1_ADDRESS'),
    },
]

# Users
users = [
    {
        'name': getenv('USER_1_NAME'),
        'address': getenv('USER_1_ADDRESS'),
        'privateKey': getenv('USER_1PRIVATE_KEY'),
        'teams': [ t for t in teams if t['userAddress'] == getenv('USER_1_ADDRESS') ]
    },
]

# Contract
contract = {
    'address': '0x82a85407bd612f52577909f4a58bfc6873f14da8',
    'abi': rootDir + '/contracts/abi-crabada.json'
}

# RPC
nodeUri = getenv('WEB3_NODE_URI')