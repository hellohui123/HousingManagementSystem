import jsonpickle


def uname_context_processor(request):
    user_str =request.session.get('user_str','')
    if user_str:
        user_obj =jsonpickle.loads(user_str)
        uname = user_obj.uname
        return {'uname':uname}
    return {'uname':''}
