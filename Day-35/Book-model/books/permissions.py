# books/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Allow read-only requests for everyone.
    Allow create/update for authenticated users.
    Allow DELETE only for staff (admin).
    """
    def has_permission(self, request, view):
        # Safe methods allowed
        if request.method in SAFE_METHODS:
            return True

        # DELETE requires staff
        if request.method == "DELETE":
            return bool(request.user and request.user.is_authenticated and request.user.is_staff)

        # Other write methods require authentication
        return bool(request.user and request.user.is_authenticated)
