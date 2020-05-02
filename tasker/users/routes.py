
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, current_user, login_required, logout_user


# helper functions
from tasker.users.forms import LoginForm, RegisterForm
from tasker.models import User


class UsersView:
    title: str

    def login(self):
        """User login view controller"""
        title: str = 'Log In'
        form = LoginForm()
        if current_user.is_authenticated:
            flash('You are already signed in.')
            return redirect(url_for('MainView:index'))

        if form.validate_on_submit():
            user = User.get_user_by_username(form.username.data)
            if user is None or not user.check_password_hash(form.password.data):
                flash('Invalid credentials. Please try again.')
                return redirect(url_for('login'))

            login_user(user=user, remember=form.remember.data)
            return redirect(url_for('MainView:index'))

        return render_template('auth/login.html', form=form, title=title)

    @login_required
    def logout(self):
        """Users logout view controller"""
        logout_user()
        flash('You were successfully logged out.')
        return redirect(url_for('MainView:index'))

    def register(self):
        """Users registration view controller"""
        form = RegisterForm()
        title = 'Register'

        if form.validate_on_submit():
            user = User.save(form.username.data, email=form.email.data, password=form.password.data)
            flash('New user - {} is registered successfully.'.format(user.username))
            return redirect(url_for('login'))

        return render_template('auth/register.html', title=title, form=form)

    @login_required
    def user_profile(self, username: str):
        """"Users profile page view controller"""
        self.title = 'Users Profile'
        user = User.get_user_by_username(username)

        return render_template('auth/users_profile.html', title=self.title, user=user)
