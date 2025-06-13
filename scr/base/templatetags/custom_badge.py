from django import template

register = template.Library()

@register.filter
def status_badge(status):
    badge_classes = {
        'Pending': 'bg-warning',
        'Received': 'bg-info',
        'In progress': 'bg-primary',
        'Completed': 'bg-success',
        'Cancelled': 'bg-danger',
    }
    badge_class = badge_classes.get(status, 'badge-secondary')  # Default to 'badge-secondary' if status not found
    return f'<span class="badge {badge_class}">{status}</span>'

@register.filter
def custom_badge_work(status):
    """
    Returns the custom CSS class for the work status
    """
    classes = {
        "En progreso": "bg-warning text-dark",
        "Esperando Repuestos": "bg-info",
        "Completado": "bg-success",
    }
    return classes.get(status, "bg-secondary")