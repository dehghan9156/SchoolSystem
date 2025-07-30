from rest_framework import permissions
from rest_framework.permissions import DjangoObjectPermissions,DjangoModelPermissions
class IsTeacherUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only access is allowed for authenticated users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.role == "teacher" or request.user.role=="admin")

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (request.user.role == "teacher" or request.user.role=="admin")
    
class IsStudentUser(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Read-only access is allowed for authenticated users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "student"
    
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and request.user.role=="student"



class IsTeacherOfClass(DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return request.user.has_perm("is_teacher", obj)

class IsStudentOfClass(DjangoObjectPermissions):
    def has_object_permission(self, request, view, obj):
        if not super().has_object_permission(request, view, obj):
            return False
        return request.user.has_perm("is_student", obj)