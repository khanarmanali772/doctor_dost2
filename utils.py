from storage import load_db, save_db

class Doctor:
    def __init__(self, d):
        self.id = d["id"]
        self.name = d["name"]
        self.specialty = d["specialty"]
        self.slots = d.get("slots", [])


def get_doctors():
    return [Doctor(d) for d in load_db()["doctors"]]


def add_patient_if_missing(name, phone):
    db = load_db()
    for p in db["patients"]:
        if p["phone"] == phone:
            return p["id"]

    pid = f"p{len(db['patients'])+1}"
    db["patients"].append({"id": pid, "name": name, "phone": phone})
    save_db(db)
    return pid


def book_appointment(did, pid, slot, notes):
    db = load_db()

    # ⭐⭐⭐ ADD START (id add kiya, logic same)
    aid = f"a{len(db['appointments'])+1}"
    # ⭐⭐⭐ ADD END

    db["appointments"].append({
        "id": aid,              # ⭐ ADD
        "doctor_id": did,
        "patient_id": pid,
        "slot": slot,
        "notes": notes
    })

    for d in db["doctors"]:
        if d["id"] == did and slot in d["slots"]:
            d["slots"].remove(slot)

    save_db(db)


# ⭐⭐⭐ ADD NEW FUNCTION (kuch delete nahi)
def cancel_appointment(aid):
    db = load_db()
    db["appointments"] = [
        a for a in db["appointments"] if a["id"] != aid
    ]
    save_db(db)
