import re

from rest_framework.serializers import ValidationError


class TitleValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        """Метод для блокировки создания объектов с левыми символами в названии"""
        reg = re.compile('^[a-zA-Z0-9\.\-\ ]+$') # это - "регулярное выражение"
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Title is not ok')
