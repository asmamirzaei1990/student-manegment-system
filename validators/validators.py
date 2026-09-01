import re
from exceptions import ValidationError

def required(value, field):
    if value is None or not str(value).strip(): raise ValidationError(f"{field} is required.")

def positive_int(value, field):
    try: value=int(value)
    except (TypeError,ValueError): raise ValidationError(f"{field} must be an integer.")
    if value <= 0: raise ValidationError(f"{field} must be positive.")
    return value

def range_float(value, low, high, field):
    try:value=float(value)
    except (TypeError,ValueError):raise ValidationError(f"{field} must be a number.")
    if not low <= value <= high:raise ValidationError(f"{field} must be between {low} and {high}.")
    return value

def email(value):
    if value and not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", value):raise ValidationError("Invalid email format.")
