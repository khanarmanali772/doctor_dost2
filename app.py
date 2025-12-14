from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import pathlib
from datetime import datetime, timedelta

from utils import get_doctors, add_patient_if_missing, book_appointment, cancel_appointment
from storage import load_db, save_db

app = Flask(__name__)
app.secret_key = "admin-secret-123"

# hashed password
ADMIN_PASSWORD_HASH = generate_password_hash("admin123")


# ================= HOME =================
@app.route("/")
def index():
    return render_template("index.html", doctors=get_doctors())


# ================= BOOK =================
@app.route("/book/<doctor_id>", methods=["GET", "POST"])
def book(doctor_id):
    doctor = next((d for d in get_doctors() if d.id == doctor_id), None)
    if not doctor:
        flash("Doctor not found", "error")
        return redirect("/")

    if request.method == "POST":
        pid = add_patient_if_missing(
            request.form["name"],
            request.form["phone"]
        )
        book_appointment(
            doctor_id,
            pid,
            request.form["slot"],
            request.form.get("notes")
        )
        return redirect("/success")

    return render_template("book.html", doctor=doctor)


# ================= SUCCESS =================
@app.route("/success")
def success():
    return render_template("success.html")


# ================= APPOINTMENTS =================
@app.route("/appointments")
def appointments():
    db = load_db()
    return render_template(
        "appointments.html",
        appointments=db.get("appointments", []),
        doctors={d["id"]: d for d in db["doctors"]},
        patients={p["id"]: p for p in db["patients"]}
    )


# ================= CANCEL APPOINTMENT (6️⃣) =================
@app.route("/appointments/cancel/<aid>")
def cancel(aid):
    cancel_appointment(aid)
    flash("Appointment cancelled", "success")
    return redirect("/appointments")


# ================= CONTACT =================
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Message sent successfully!", "success")
    return render_template("contact.html")


# ================= ADMIN LOGIN =================
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if check_password_hash(ADMIN_PASSWORD_HASH, request.form["password"]):
            session["admin"] = True
            return redirect("/admin")
        flash("Wrong password", "error")
    return render_template("admin_login.html")


# ================= ADMIN LOGOUT (7️⃣) =================
@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect("/")


# ================= ADMIN DASHBOARD =================
@app.route("/admin")
def admin():
    if not session.get("admin"):
        return redirect("/admin/login")
    return render_template("admin_dashboard.html", doctors=load_db()["doctors"])


# ================= ADD DOCTOR =================
@app.route("/admin/add-doctor", methods=["POST"])
def add_doctor():
    if not session.get("admin"):
        return redirect("/admin/login")

    db = load_db()
    db["doctors"].append({
        "id": f"d{len(db['doctors'])+1}",
        "name": request.form["name"],
        "specialty": request.form["specialty"],
        "slots": []
    })
    save_db(db)
    return redirect("/admin")


# ================= EDIT DOCTOR (9️⃣) =================
@app.route("/admin/edit-doctor/<did>", methods=["GET", "POST"])
def edit_doctor(did):
    if not session.get("admin"):
        return redirect("/admin/login")

    db = load_db()
    doctor = next(d for d in db["doctors"] if d["id"] == did)

    if request.method == "POST":
        doctor["name"] = request.form["name"]
        doctor["specialty"] = request.form["specialty"]
        save_db(db)
        return redirect("/admin")

    return render_template("admin_edit_doctor.html", doctor=doctor)


# ================= DELETE DOCTOR =================
@app.route("/admin/delete-doctor/<did>")
def delete_doctor(did):
    if not session.get("admin"):
        return redirect("/admin/login")

    db = load_db()
    db["doctors"] = [d for d in db["doctors"] if d["id"] != did]
    save_db(db)
    return redirect("/admin")


# ================= SLOT GENERATE =================
@app.route("/admin/generate-slots/<doctor_id>")
def generate_slots(doctor_id):
    if not session.get("admin"):
        return redirect("/admin/login")

    db = load_db()
    for d in db["doctors"]:
        if d["id"] == doctor_id:
            slots = []
            now = datetime.now()
            for i in range(5):
                day = now + timedelta(days=i)
                for h in [10, 12, 14, 16]:
                    slots.append(day.strftime(f"%Y-%m-%d {h}:00"))
            d["slots"] = slots
    save_db(db)
    return redirect("/admin")


# ================= API (🔟 React Ready) =================
@app.route("/api/doctors")
def api_doctors():
    return jsonify(load_db()["doctors"])


if __name__ == "__main__":
    pathlib.Path("data").mkdir(exist_ok=True)
    app.run(debug=True)
