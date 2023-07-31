import os
import logging
from datetime import datetime

cwd = os.getcwd()
log_dir = cwd + '/log/'
error_dir = cwd + '/error/'
now = datetime.today()
today = now.strftime('%Y%m%d')
log_filename = today + '.log'

if not os.path.isdir(log_dir):
    os.mkdir(log_dir)

if not os.path.isdir(error_dir):
    os.mkdir(error_dir)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

fh = logging.FileHandler(log_dir + log_filename)
fh.setLevel(logging.DEBUG)

ch = logging.FileHandler(error_dir + log_filename)
ch.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

def error_log(message):
    logger.error(message)

def info_log(message):
    logger.info(message)

def debug_log(message):
    logger.debug(message)
