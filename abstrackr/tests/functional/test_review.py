from abstrackr.tests import TestController, url

#from nose.tools import ok_            # This is shorthand for assert

from nose.plugins.attrib import attr  # Decorator to mark tests
                                      # Use ``nosetests -a author=jj`` to
                                      # run only marked tests or 
                                      # ``nosetests -a '!author=jj`` to
                                      # exclude marked tests


class TestReviewController(TestController):

    @attr(author='jj', controller='account')
    def test_create_account(self):
        """ Create account

        Since the database has just been rebuild it lacks any
        user to run tests with. We will test the create_account
        action in the account controller to help us create a test
        user to run further tests.

        """

        # Get the `create_account` page.
        response = self.app.get(
                url(controller='account', action='create_account'),
                status=200)
        # Make sure it has the correct url.
        assert response.req.environ['PATH_INFO'] == '/account/create_account'
        # Fill out the create account form.
        form = response.form
        form['first_name'] = u'tester'
        form['last_name'] = u'bot'
        form['experience'] = u'5'
        form['email'] = u'tester_bot@brown.edu'
        form['username'] = u'tester'
        form['password'] = u'tester'
        # Submit the form and throw if status not 302.
        post_submit = form.submit(status=302)
        # Submitting the form directs us back to `login` page. Let's follow.
        post_submit = post_submit.follow(status=302)
        # Since we are now registered, `login` page will redirect to
        # `welcome` page
        post_login = post_submit.follow(status=302)
        # `Welcome` page redirects to `my_work` page; let's follow that also
        # The `my_work` page gets rendered based on how many outstanding
        # assignments the user has, therefore we should check that this has
        # status 200
        post_login = post_login.follow(status=200)
        # Since this is a brand new account, let's check that we get the
        # "Hurray...." message
        assert "hurray, you've no outstanding assignments" in post_login


    @attr(author='jj', controller='review')
    def test_create_new_review(self):
        """ Anonymous users should be asked to log in

        User should be redirected to login screen.
        After login, verify that the correct page was rendered.

        """

        response = self.app.get(
                url(controller='review', action='create_new_review'),
                status=302)
        response = response.follow(status=200)
        form = response.form
        form['login'] = u'tester'
        form['password'] = u'tester'
        response = form.submit(status=302)
        # Several redirects we need to navigate through
        response = response.follow(status=302)
        response = response.follow(status=200)
        # Verify path is correct
        assert response.req.environ['PATH_INFO'] == '/review/create_new_review'
        # Verify that several keywords show up on the page
        assert 'project name' in response
        assert 'project description' in response
        assert 'upload file' in response
        assert 'screening mode' in response
        assert 'order abstracts by' in response
        assert 'pilot round size' in response
        assert 'tag visibility' in response

    @attr(author='jj', controller='review')
    def test_predictions_about_remaining_citations(self):
