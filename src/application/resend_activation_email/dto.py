from dataclasses import dataclass

from src.domain.models.email import Email


@dataclass(frozen=True)
class ResendActivationEmailDTO:
    user_email: Email
