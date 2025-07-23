import boto3
import os
import logging

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger()


class DBConnection:

    def db_Connector (table_name_val):

#Use this to test locally , in AWS we don't need to add this as Lambda will automatically use the ap gateway users
        """session = boto3.Session(
            aws_access_key_id='###',
            aws_secret_access_key='####',
            region_name='####'
        )"""

        logger.info(f"Invoking dynamoDB {table_name_val} ")
        #dynamodb = session.resource('dynamodb')
        dynamodb = boto3.resource('dynamodb')
        table_name= os.environ.get('TABLE_NAME', table_name_val)
        table= dynamodb.Table(table_name)
        logger.info(f"DB invoke successful for {table_name_val}")
        return table






