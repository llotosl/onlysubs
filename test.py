import abc
from typing import Annotated

from fastapi import Depends


class User:
    telegram: str | None
    email: str | None
    phone_number: str | None
    vk_id: str | None


class UserNotificator(abc.ABC):
    @abc.abstractmethod
    def send_message_to_user(self, user: User, message: str) -> None:
        raise NotImplementedError


class EmailUserNotificator(UserNotificator):
    def send_message_to_user(self, user: User, message: str) -> None:
        email = user.email
        if email is None:
            raise ValueError
        # send email


class TelegramNotificator(UserNotificator):
    def send_message_to_user(self, user: User, message: str) -> None:
        tg = user.telegram
        if tg is None:
            raise ValueError
        # send tg message


class UserNotificatorFactory(abc.ABC):
    @abc.abstractmethod
    def create_notificator_from_user(self, user: User) -> UserNotificator:
        raise NotImplementedError


class UserNotificatorFactoryImpl(UserNotificatorFactory):
    def create_notificator_from_user(self, user: User) -> UserNotificator:
        if user.email is not None:
            return EmailUserNotificator()

        if user.telegram is not None:
            return TelegramNotificator()

        raise ValueError


def some_endpoint_with_notification(
    notification_factory: Annotated[UserNotificatorFactory, Depends()],
    current_user: Annotated[User, Depends()],
) -> None:
    notificator = notification_factory.create_notificator_from_user(current_user)
    notificator.send_message_to_user(current_user, "Hello, user!")
