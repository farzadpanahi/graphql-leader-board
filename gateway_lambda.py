from sleemo.framework import get_appsync_framework

sleemo = get_appsync_framework(resolver_path='resolvers')


@sleemo.default_gateway()
def handler(event, context):
    return sleemo.resolve(event)
