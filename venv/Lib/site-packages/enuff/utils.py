def ensure_pk(instance):
    if not instance:
        return instance
    try:
        return int(instance)
    except ValueError:
        return instance.pk
