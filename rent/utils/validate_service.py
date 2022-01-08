def validate_rent_service(attrs):
    if 'name' in attrs > 1:
        return "Name must be more than 1 charter"
    else:
        pass
