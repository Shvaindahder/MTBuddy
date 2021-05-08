from flask import redirect, render_template
from flask_login import login_required

from app.meeting import bp
from app.meeting.forms import CreateMeetingForm


@login_required
@bp.route("create-meeting", methods=["GET", "POST"])
def create_meeting():
    form = CreateMeetingForm()
    if form.validate_on_submit():
        pass
    context = {
        "title": "Create a meeting",
        "form": form
    }
    return render_template("meeting/create_meeting.html", **context)


@login_required
@bp.route("join-meeting")
def join_meeting():
    pass


@login_required
@bp.route("activities")
def activities():
    pass


@login_required
@bp.route("bike-rent")
def bike_rent():
    pass