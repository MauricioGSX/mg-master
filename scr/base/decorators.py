from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

def group_required(group_name):
    """
    Decorator that restricts access to a view based on user group membership.

    Parameters:
        group_name (str): The name of the group required to access the view.

    Returns:
        function: A wrapped view that checks if the user belongs to the specified group.
                  If not, returns a 403 Forbidden response.

    Usage:
        @group_required('admin')
        def my_view(request):
            ...
    """
    def decorator(view_func):
        @wraps(view_func)
        @login_required  # Ensures the user is authenticated before checking group
        def _wrapped_view(request, *args, **kwargs):
            # Check if the authenticated user belongs to the required group
            if not request.user.groups.filter(name=group_name).exists():
                return HttpResponseForbidden(
                    "You do not have permission to access this page."
                )
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator
