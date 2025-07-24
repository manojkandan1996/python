from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.user import User
from app.forms.user_form import UserEditForm
from run import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import logging

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    form = UserEditForm(obj=user)  # Pre-fill with current data

    if form.validate_on_submit():
        # Log before
        logging.warning(f"[AUDIT] Before update: {user.__dict__}")

        user.name = form.name.data
        user.email = form.email.data
        user.is_active = form.is_active.data

        # Password change logic
        if form.new_password.data:
            if not form.current_password.data:
                flash("Current password required to change password", "danger")
                return redirect(url_for('user.edit_user', id=id))
            if not check_password_hash(user.password_hash, form.current_password.data):
                flash("Current password is incorrect", "danger")
                return redirect(url_for('user.edit_user', id=id))
            user.password_hash = generate_password_hash(form.new_password.data)

        db.session.commit()

        # Log after
        logging.warning(f"[AUDIT] After update: {user.__dict__}")

        flash("User updated successfully", "success")
        return redirect(url_for('user.edit_user', id=id))

    return render_template('user/edit_user.html', form=form, user=user)
