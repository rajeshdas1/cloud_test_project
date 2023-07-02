import logging
import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Lambda triggered at {0}".format(datetime.datetime.now()))
    print("success")
    return 'SUCCESS'


if __name__ == '__main__':
    lambda_handler({}, None)
    