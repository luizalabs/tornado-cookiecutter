from restless.exceptions import NotFound

from .session import session


def get_or_404(_model, id, bind=None):
    """
    Return object or not found exception

    :param _model: Model
    :param id: Primary key
    :param bind: Name of other engine

    Example:

        # without bind
        food = get_or_404(Food, 1)
        food.name
        >>> Espinafre

        # with bind
        food = get_or_404(Food, 1, 'other1')
        food.name
        >>> CuzCuz

        # not found
        food = get_or_404(Food, 42)
        # { "error": "Food not found" }
    """
    if bind:
         obj = session.using(bind).query(_model).get(id)
    else:
        obj = session.query(_model).get(id)

    if obj:
        return obj
    else:
        raise NotFound('{0} not found'.format(_model.__name__))
