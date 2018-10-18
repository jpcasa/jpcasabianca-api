from rest_framework.permissions import BasePermission

from . import models


class IsOwner(BasePermission):
    """Custom permission class to allow only menu owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, models.Menu):
            return obj.owner == request.user
        return obj.owner == request.user


class IsOwnerMenuItem(BasePermission):
    """Custom permission class to allow only menu owners to edit them."""

    def has_object_permission(self, request, view, obj):
        """Return True if permission is granted to the bucketlist owner."""
        if isinstance(obj, models.MenuItem):
            return obj.owner == request.user
        return obj.owner == request.user
