from datetime import UTC, datetime

from onlysubs.domain.models.email import Email
from onlysubs.domain.models.user import HashedPassword, User, Username


def create_user(is_active: bool = True) -> User:
    now = datetime.now(UTC)

    return User(
        username=Username("test"),
        email=Email("test@test.com"),
        first_name="test",
        last_name="test",
        password=HashedPassword("<PASSWORD>"),
        is_active=True,
        created_at=now,
        updated_at=now,
    )
