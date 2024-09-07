from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from onlysubs.domain.models.user import UserId


@dataclass
class UserActivation:
    user_id: UserId
    active_till: datetime


UserActivationToken = NewType("UserActivationToken", str)
