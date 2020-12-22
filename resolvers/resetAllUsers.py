from resolvers._resolver_helper import get_user_table


def resetAllUsers(event):
    user_table = get_user_table()
    users = user_table.get_all_users()

    for user in users:
        user.points = 0
        result = user_table.update_user(user)  # TODO: this is not really efficient
        if result is False:
            return False

    return True
