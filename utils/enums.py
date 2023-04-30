import enum


# Criterion types
class CriterionTypes(str, enum.Enum):
    completed = "completed"
    pending = "pending"
    canceled = "canceled"
    all = "all"
