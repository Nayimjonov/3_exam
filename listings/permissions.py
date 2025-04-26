from rest_framework import permissions
from .models import Listing

class IsListingOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        listing_id = view.kwargs.get('listing_id')
        if not listing_id:
            return False
        listing = Listing.objects.filter(id=listing_id, seller=request.user).exists()
        return listing

    def has_object_permission(self, request, view, obj):
        return obj.listing.seller == request.user