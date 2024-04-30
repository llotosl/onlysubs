from dataclasses import dataclass

from onlysubs.domain.models.email import Email


@dataclass(frozen=True)
class ResendActivationEmailDTO:
    user_email: Email
