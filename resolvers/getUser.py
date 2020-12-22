from resolvers._resolver_helper import get_user_table


def getUser(id, event):
    user_table = get_user_table()
    user = user_table.get_user(user_id=id)
    if user is None:
        return None

    return user.to_dict()

