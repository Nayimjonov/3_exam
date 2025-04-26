from rest_framework import permissions
from .models import Listing

class IsListingOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of a listing to edit it.
    """

    def has_permission(self, request, view):
        listing_id = view.kwargs.get('listing_id')
        if not listing_id:
            return False
        listing = Listing.objects.filter(id=listing_id, seller=request.user).exists()
        return listing

    def has_object_permission(self, request, view, obj):
        # Allow only if the user is owner of the listing
        return obj.listing.seller == request.user