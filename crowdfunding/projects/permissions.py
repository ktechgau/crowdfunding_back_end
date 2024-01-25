from rest_framework import permissions

class IsOwnerOrReadOnlyProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsOwnerOrReadOnlyPledge(permissions.BasePermission):    ##created this seperate permissions class for pledges
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.supporter == request.user


