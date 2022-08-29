from django.core.exceptions import PermissionDenied

def decorator_admin_protect(func):
    def _decorator(self, *args, **kwargs):
        if (self.request.user.is_superuser):
            return func(self, *args, **kwargs)
        raise PermissionDenied("Need to be admin to access this route")
    return _decorator