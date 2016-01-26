import tornado.web


class UserAuthentication(tornado.web.RequestHandler):
    def head(self):
        """Authentication user (sign in)

        Returns:
            http headers. 404: not found, 403: disabled, 200: signed in.
        """
        username = self.get_argument('username')
        password = self.get_argument('password')
        if not username or not password:
            self.set_status(403)
        # Check Authentication FIXME

    def get(self):
        pass

    def post(self):
        """Register user (sign up)

        Returns:
            JSON string which contain status. example: {"status": "ok"},
            {"status": "failed"}, {"status": "exists"}
        """
        username = self.get_argument('username')
        email = self.get_argument('email')
        password = self.get_argument('password')
        # It should check that username is not be "list" <<<
        # Token generator
        # Reigster user
        # send activation email


class UserInformation(tornado.web.RequestHandler):
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


class UserToken(tornado.web.RequestHandler):
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


class Help(tornado.web.RequestHandler):
    def get(self):
        """Show how to work with API for users part.

        Returns:
            HTML tags and colorize output.
        """
        # Create html output for better helping developers.
        pass
