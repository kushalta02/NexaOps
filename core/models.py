from dataclasses import dataclass

@dataclass
class Incident:
    incident_id: str
    system:str
    desc:str
    status:str = "open"