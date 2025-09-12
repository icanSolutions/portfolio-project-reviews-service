from app.errors import ReviewNotFoundError

def get_or_404(model, obj_id=None, **filters):
    query = model.query

    # Apply filters if provided
    if filters:
        query = query.filter_by(**filters).first()

    # If obj_id is provided, look by primary key
    if obj_id is not None:
        instance = query.get(obj_id)
    else:
        instance = query.first()

    if not instance:
        raise ReviewNotFoundError(
            f"{model.__name__} with filters {filters or {'id': obj_id}} not found"
        )
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