from datetime import datetime

from flask import redirect, render_template, url_for, request, jsonify
from flask_login import login_required, current_user

from app import db
from app.meeting import bp
from app.meeting.forms import CreateMeetingForm
from models.user import User
from models.meeting import Meeting


@login_required
@bp.route("create-meeting", methods=["GET", "POST"])
def create_meeting():
    form = CreateMeetingForm()
    if form.validate_on_submit():
        meeting = Meeting(
            meeting_creator=current_user.id,
            max_bikers=form.num_of_bikers.data,
            area=form.area.data,
            trail=form.trail.data,
            date_time=datetime.fromisoformat(f"{form.date.data} {form.time.data}"),
            title=form.title.data,
            description=form.description.data,
            min_skill=form.min_skill.data
        )
        db.session.add(meeting)
        current_user.participations.append(meeting)
        db.session.commit()
        return redirect(url_for("main.profile"))

    context = {
        "title": "Create a meeting",
        "form": form
    }
    return render_template("meeting/create_meeting.html", **context)


@login_required
@bp.route("join-meeting")
def join_meeting():
    args  = request.args

    area  = args.get('area', None)
    date  = args.get('date', None)
    skill = args.get('skill', None)

    query = Meeting.query
    if area is not None:
        query = query.filter_by(area=area)
    
    if date is not None:
        query = query.filter(Meeting.date_time > datetime.fromisoformat(date))

    if skill is not None:
        query = query.filter(Meeting.min_skill <= skill)

    meetings = query.all()

    context = {
        "title": "Join a meeting",
        "meetings": meetings
    }
    return render_template("meeting/join_meeting.html", **context)


@bp.route("/join", methods=["POST"])
def join():
    meeting_id = request.args.get("meeting_id", None)
    if meeting_id is None:
        return jsonify({"status": "failed"})
    meeting = Meeting.query.get(meeting_id)
    if current_user.skill_level >= meeting.min_skill:
        current_user.participations.append(Meeting.query.get(meeting_id))
        db.session.commit()
        return jsonify({"status": "success"})
    return jsonify({"status": "failed"})


@login_required
@bp.route("activities")
def activities():
    meetings = sorted(current_user.participations, key=lambda x: x.date_time, reverse=True)
    context = {
        "title": "Activities",
        "meetings": meetings
    }
    return render_template("meeting/activities.html", **context)


@login_required
@bp.route("cancel-paricipition", methods=["POST"])
def cancel_participition():
    meeting_id = request.args.get("meeting_id", None)
    if meeting_id is None:
        return jsonify(
            {"status": "failed", "message": "No miting_id arg in request."}
        )

    participations_count = len(current_user.participations)
    current_user.participations = list(filter(lambda x: x.id != meeting_id, current_user.participations))
    if len(current_user.participations) == participations_count:
        return jsonify(
            {"status": "failed", "message": "You are not a participant in the meeting {meeting_id}"}
        )
    db.session.commit()
    return jsonify({"status": "success"})

    


@login_required
@bp.route("bike-rent")
def bike_rent():
    return render_template("meeting/bike_rent.html")