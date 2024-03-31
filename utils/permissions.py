from rest_framework import permissions


class IsAuthorGroup(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='AuthorGroup'):
            return True
        return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the blog.
        return obj.author == request.user or request.user.is_superuser 
