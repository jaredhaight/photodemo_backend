from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Allow access for SAFE_METHODS (GET, HEAD or OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        #For the rest, only allow if obj.owner = user
        return obj.author == request.user

