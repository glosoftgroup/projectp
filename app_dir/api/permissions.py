from structlog import get_logger
from rest_framework import permissions
from rolepermissions.checkers import has_permission as role_perms


class IsPermittedCreateView(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if role_perms(user, 'can_create_view_via_API'):
            return True
        return False

