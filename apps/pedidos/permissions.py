from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user


class IsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        message = 'Você precisa estar logado !'
        esta = bool(request.user and request.user.is_authenticated)
        if esta:
            return esta
        else:
            raise PermissionDenied(detail=message)