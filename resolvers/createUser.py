import uuid
from models.user import User
from resolvers._resolver_helper import get_user_table


def createUser(input, event):
    user_table = get_user_table()
    new_user = User(
        id=str(uuid.uuid4()),
        name=input['name'] if 'name' in input else None,
        age=input['age'] if 'age' in input else None,
        address=input['address'] if 'address' in input else None
    )

    result = user_table.put_user(new_user)

    if not result:
        raise Exception('Failed to create user')

    return new_user.to_dict()

