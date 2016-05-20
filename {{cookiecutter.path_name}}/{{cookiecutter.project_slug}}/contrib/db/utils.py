from restless.exceptions import NotFound

from .session import session


def get_or_404(_model, id):
    obj = session.query(_model).get(id)

    if obj:
        return obj
    else:
        raise NotFound('{0} not found'.format(_model.__name__))
