import boto3
import configparser
from models.user import User

from botocore.exceptions import ClientError

config = configparser.ConfigParser()
config.read('config.ini')


class UserTable:
    def __init__(self, region, table_name):
        self.table = self._get_table(region, table_name)

    @staticmethod
    def _get_table(region, table_name):
        dynamodb = boto3.resource('dynamodb', region_name=region)
        return dynamodb.Table(table_name)

    def get_user(self, user_id):
        try:
            response = self.table.get_item(Key={'id': user_id})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return self._parse_ddb_item(response['Item'])

    def get_all_users(self):
        try:
            response = self.table.scan()  # TODO: this is just a temp solution; 10MB limit
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return [self._parse_ddb_item(item) for item in response['Items']]

    def put_user(self, user: User):
        try:
            response = self.table.put_item(Item={
                'id': user.id,
                'name': user.name,
                'age': user.age,
                'address': user.address,
                'points': user.points
            })
        except ClientError as e:
            print(e.response['Error']['Message'])
            return False

        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    def update_user(self, user: User):
        try:
            response = self.table.update_item(
                Key={'id': user.id},
                UpdateExpression="set #nm=:n, age=:a, address=:ad, points=:p",
                ExpressionAttributeValues={
                    ':n': user.name,
                    ':a': user.age,
                    ':ad': user.address,
                    ':p': user.points
                },
                ExpressionAttributeNames={
                    '#nm': 'name'
                }
            )

        except ClientError as e:
            print(e.response['Error']['Message'])
            return False

        return response['ResponseMetadata']['HTTPStatusCode'] == 200

    @staticmethod
    def _parse_ddb_item(item):
        if item is None:
            return None

        return User(
            id=item['id'] if 'id' in item else None,
            name=item['name'] if 'name' in item else None,
            age=int(item['age']) if 'age' in item else None,
            address=item['address'] if 'address' in item else None,
            points=int(item['points']) if 'points' in item else None
        )
