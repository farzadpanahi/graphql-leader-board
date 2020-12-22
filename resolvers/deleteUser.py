from resolvers._resolver_helper import get_user_table


def deleteUser(input, event):
    user_table = get_user_table()
    result = user_table.delete_user(input['id'])

    return result
