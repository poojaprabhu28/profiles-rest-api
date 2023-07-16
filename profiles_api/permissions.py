from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check User is trying to edit their own profile"""
        # safe methods are those that don't make any changes
        if request.method in permissions.SAFE_METHODS:            
            return True
        
        #ensure user has same id as the one registered in the system
        return obj.id == request.user.id
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the users is trying to update their own status"""
        if request.method  in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id