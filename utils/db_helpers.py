from app.errors import ReviewNotFoundError

def get_or_404(model, obj_id):
    if obj_id:
        instance = model.session.get(obj_id)
        if not instance:
            raise ReviewNotFoundError(f"{model.__name__} with ID {obj_id} not found")
    else:
        instance = model.query.all()
        if not instance:
            raise ReviewNotFoundError(f"{model.__name__}s not found")
    return instance

def get_list_or_404(model, field=None, value=None):
    if field and value:
        column = getattr(model, field)
        if not column:
            raise ValueError(f"{field} is not a valid field of {model.__name__}")
        instances = model.query.filter(column == value).all()
    else:
        instances = model.query.all()
    if not instances:
            raise ReviewNotFoundError(f"No {model.__name__} founded")
    return instances