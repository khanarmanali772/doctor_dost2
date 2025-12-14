from dataclasses import dataclass, asdict
from typing import Optional
import uuid

def gen_id(prefix: str) -> str:
    return f"{prefix}{uuid.uuid4().hex[:8]}"

@dataclass
class Doctor:
    id: str
    name: str
    specialty: str
    slots: list[str]

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["id"], d["name"], d["specialty"], d.get("slots", []))

    def to_dict(self):
        return asdict(self)

@dataclass
class Patient:
    id: str
    name: str
    phone: str

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["id"], d["name"], d["phone"])

    def to_dict(self):
        return asdict(self)

@dataclass
class Appointment:
    id: str
    doctor_id: str
    patient_id: str
    slot: str
    notes: Optional[str] = None

    @classmethod
    def from_dict(cls, d: dict):
        return cls(d["id"], d["doctor_id"], d["patient_id"], d["slot"], d.get("notes"))

    def to_dict(self):
        return asdict(self)
