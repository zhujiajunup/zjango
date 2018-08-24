

def print_user(backend, uid, user=None, *args, **kwargs):
    request = kwargs['request']



def check(*args, **kwargs):
    print(kwargs['user'])


def social_user(backend, uid, user=None, *args, **kwargs):
    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        user = social.user

    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': social is None}
