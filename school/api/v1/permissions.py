from rest_framework import permissions

class IsTeacherUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only access is allowed for authenticated users.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role=="teacher"
    
class IsStudentUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only access is allowed for authenticated users.
    """
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role=="student"