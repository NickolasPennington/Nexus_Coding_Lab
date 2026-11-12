import json
import os

AUDIT_FILE = "audit_file.json"

class AuditRecord:
    def __init__(self, customer_id, actor_id, reason):
        self.customer_id = customer_id
        self.actor_id = actor_id
        self.reason = reason


class Auditor:
    def __init__(self):
        self.records = []

        if os.path.exists(AUDIT_FILE):
            with open(AUDIT_FILE, "r") as audit_file:
                for line in audit_file:
                    record_dict = json.loads(line)
                    record = AuditRecord(**record_dict)
                    self.records.append(record)


    def add_record(self, record):
        self.records.append(record)

        with open(AUDIT_FILE, "a+") as audit_file:
            audit_file.write(json.dumps(record.__dict__) + "\n")
            

    def get_all(self):
        list_of_record_dicts = []

        for record in self.records:
            list_of_record_dicts.append(record.__dict__)

        return list_of_record_dicts

            