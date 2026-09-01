class AppError(Exception): pass
class NotFoundError(AppError): pass
class DuplicateError(AppError): pass
class ValidationError(AppError): pass
class CapacityError(AppError): pass
class ConflictError(AppError): pass
