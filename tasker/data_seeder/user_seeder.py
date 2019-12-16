from tasker.models import User


class UsersSeeder:
    """Users seder provides sample  users for application testing"""
    username: str = 'john'
    email: str = 'john@exmaple.com'
    password: str = 'john123'

    def find_user(self, username: str):
        """Finds user from db. """
        return User.get_user_by_username(username)

    def create_user(self, username: str = None, email: str = None, password: str = None) -> User:
        """
        Creates new user for testing  and experimenting
        @param username: str
        @param email: str
        @param password: str
        @return: User
        """
        if username is None or email is None or password is None:
            user = self.find_user(self.username)
            if user is None:
                user = User.save(self.username, self.email, self.password)
        else:
            user = self.find_user(username)
            if user is None:
                user = User.save(username, email, password)
        return user

