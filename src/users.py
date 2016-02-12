from tornado.web import RequestHandler
from src.libs import Libs


class User(RequestHandler):
    def get(self):
        """Fetch list of all users

        :return: JSON string which contains all users with their status.
        :rtype: str
        """
        users = Libs.get_users_list()
        self.write(str(users))


class UserAuthentication(RequestHandler):
    def get(self):
        """Authentication user (sign in)

        :return: JSON string which contain status. example: {"status": "ok"}, {"status": "no"}
        :rtype: str
        """
        data = {"status": "no"}
        username = self.get_argument('username')
        password = self.get_argument('password')
        if not username or not password:
            self.write(data)
        record = Libs.authentication(username, password)

        if record:
            if record.get("is_lock") is True:
                data["status"] = "locked"
            elif record.get("is_active") is False:
                data["status"] = "deactivated"
            else:
                data["status"] = "ok"
        self.write(data)

    def post(self):
        """Register user (sign up)

        :return: JSON string which contain status.
        :rtype: str
        """
        username = self.get_argument('username')
        email = self.get_argument('email')
        password = self.get_argument('password')

        action = Libs.create_user(username, password, email)
        self.write({"status": action})


class UserInformation(RequestHandler):
    def get(self):
        """Get user information. It could be list of all users or user information.

        Args:
            arg: it should be "list" keyword which returns list of all
            users otherwise returns user details.
        Returns:
            JSON string which has "status" to determine that returned data
            is okay or not.
        """
        data = self.get_argument('data')
        if data.get('type') == "list":
            pass
            # Fetch list of all users
        else:
            pass
            # Fetch user information

    def put(self):
        """Update user information

        Args:
            arg: username or email address of user.
        Returns:
            JSON string which has "status" to tell you it's updated or not.
        """
        data = self.get_argument('data')
        # Update user information

    def delete(self):
        """Disable user status which can't user system.

        Returns:
            JSON string which has "status" to tell you it's disabled or not.
        """
        data = self.get_argument('data')
        # Disable user status


class UserToken(RequestHandler):
    def get(self):
        """Get user last token which are waiting for approval.

        Returns:
            JSON string which has "status" to tell you it's okay or not.
        """
        data = self.get_argument('data')
        # Get user token
        pass

    def post(self):
        """Generate new token for user and add it in queue.

        Returns:
            JSON string which has "status" to tell you it's okay or not.
        """
        # Generate new token and add it in queue.
        pass


class Help(RequestHandler):
    def get(self):
        """Show how to work with API for users part.

        Returns:
            HTML tags and colorize output.
        """
        # Create html output for better helping developers.
        pass
