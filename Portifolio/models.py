from typing import Iterable
from django.db import models
import uuid
from django.core.validators import FileExtensionValidator
from phonenumber_field.modelfields import PhoneNumberField
from FuncDashboard.models import Funcionario


