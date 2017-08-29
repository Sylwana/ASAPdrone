import datetime

def my_footer(request):
    return {'now' : datetime.datetime.now(), 'current_user':request.user.username, 'current_user_id': request.user.id}

