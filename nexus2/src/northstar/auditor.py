class AuditRecord:
    def __init__(self, customer_id, actor_id, reason):
        self.customer_id = customer_id
        self.actor_id = actor_id
        self.reason = reason

    def as_dict(self):
        return {
            "customer_id": self.customer_id,
            "actor_id": self.actor_id,
            "reason": self.reason
            }


class Auditor:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_all(self):
        list_of_record_dicts = []

        for record in self.records:
            list_of_record_dicts.append(AuditRecord.as_dict(record))

        return list_of_record_dicts

            