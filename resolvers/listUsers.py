from resolvers._resolver_helper import get_user_table


def listUsers(event):
    user_table = get_user_table()
    users = user_table.get_all_users()
    if users is None:
        return None

    return [user.to_dict() for user in users]