from django.db.models import Q

HARDWARE_NOTICE_ASSIGNMENT_MODELS = Q(
    Q(app_label='dcim', model='devicetype') | Q(app_label='dcim', model='inventoryitem'),
)
