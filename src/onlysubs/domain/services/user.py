import hashlib
from onlysubs.domain.dto.user import CreateUserDTO
from onlysubs.domain.models.user import HashedPassword, User


class UserService:
    def __init__(self, password_salt: str) -> None:
        self.__pasword_salt = password_salt

    def create_user(self, data: CreateUserDTO) -> User:
        return User(
            id=None,
            username=data.username,
            first_name=data.first_name,
            last_name=data.last_name,
            password=self.__hash_password(data.password),
        )

    def is_user_password_valid(self, user: User, password: str) -> bool:
        return user.password == self.__hash_password(password)

    def __hash_password(self, password: str) -> HashedPassword:
        data_to_hash = "{0}{1}".format(password, self.__pasword_salt)
        hash = hashlib.sha256(data_to_hash.encode("utf-8")).hexdigest()
        return HashedPassword(hash)
