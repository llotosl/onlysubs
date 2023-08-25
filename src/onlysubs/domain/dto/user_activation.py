from dataclasses import dataclass
from datetime import datetime

from onlysubs.domain.models.user import UserId


@dataclass
class UserActivationTokenPayloadDTO:
    user_id: UserId
    active_till: datetime
