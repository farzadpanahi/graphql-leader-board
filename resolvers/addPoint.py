from resolvers._resolver_helper import get_user_table


def addPoint(input, event):
    user_table = get_user_table()
    user = user_table.get_user(user_id=input['id'])
    if user is None:
        return False

    result = user.add_point()

    if result:
        return user_table.update_user(user)

    return False
