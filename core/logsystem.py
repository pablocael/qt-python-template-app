# Copyright (C) 2021 Pablo Carneiro Elias
#
# All rights reserved.
#
# This file is part of Template Matching Application and is property of the
# author Pablo Carneiro Elias. This file, as well as the whole it is contained
# in can only be ditributed under author's agreement.
# For further details on obtaining a commercial license, contact Pablo Carneiro Elias
# at pablo.cael@gmail.com

import os
import logging
from decouple import config
from logging.handlers import RotatingFileHandler

# Setup logging
def setup_logging_system(log_filepath):
    logFile = config('LOG_OUTPUT_FILE', default=log_filepath)
    if not os.path.isdir('logs'):
        os.mkdir('logs')

    log_level_name = config('LOG_LEVEL', default='debug').upper()
    log_handler = RotatingFileHandler(log_filepath,  maxBytes=20000000, backupCount=10)
    log_handler.setLevel(logging.getLevelName(log_level_name))

    logging.basicConfig(
            handlers=[log_handler],
            level=logging.getLevelName(log_level_name),
            format='<%(name)s>: %(asctime)s.%(msecs)d [%(levelname)s] => %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            force=True)

