from rest_framework import permissions
from .models import Listing


class IsListingOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        listing_id = view.kwargs.get('listing_id')
        if not listing_id:
            return False
        return Listing.objects.filter(id=listing_id, seller=request.user).exists()

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, 'listing'):
            return obj.listing.seller == request.user
        return obj.seller == request.user