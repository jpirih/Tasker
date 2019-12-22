from tasker.models import User
from typing import List


class UsersSeeder:
    """Users seder provides sample  users for application testing"""
    username: str = 'john'
    email: str = 'john@exmaple.com'
    password: str = 'john123'

    USERS: List = [
        {
            'username': 'ana',
            'email': 'ana@example.com',
            'password': 'ana123'
        },
        {
            'username': 'meta',
            'email': 'meta@example.com',
            'password': 'meta123'
        },
        {
            'username': 'neja',
            'email': 'neja@example.com',
            'password': 'neja123'
        },
    ]

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

    def seed_sample_users(self) -> None:
        """Provides list of 3 users for testing and sample data"""
        for user in self.USERS:
            self.create_user(username=user['username'], email=user['email'], password=user['password'])
        print('\n{} new users were saved to database.'.format(len(self.USERS)))
