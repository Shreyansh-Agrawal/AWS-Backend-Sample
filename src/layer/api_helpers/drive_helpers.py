from aws_helpers import dynamodb_helper


def get_all_drives():
    data = dynamodb_helper.query_db()
    return data


def add_drive():
    ...


def update_drive():
    ...


def delete_drive():
    ...
