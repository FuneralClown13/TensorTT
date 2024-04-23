import os
import sys

logger_config = [
    {"sink": f"{os.getcwd()}\\logs\\info.log", 'format': '{time} {level} {message}',
     'level': 'INFO', 'rotation': '1 MB', 'compression': 'zip'},
    {"sink": sys.stdout, 'format': '{time} {level} {message}',
     'level': 'INFO'}
]
