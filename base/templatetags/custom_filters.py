from django import template

register = template.Library()

@register.filter
def status_badge_class(status):
    if status == "En progreso":
        return "badge-primary"
    elif status == "Esperando Repuestos":
        return "badge-warning"
    elif status == "Completado":
        return "badge-success"
    else:
        return "badge-secondary"
