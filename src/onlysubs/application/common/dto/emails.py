from dataclasses import dataclass


@dataclass
class SendUserActivationEmailDTO:
    user_email: str
    activation_url: str
