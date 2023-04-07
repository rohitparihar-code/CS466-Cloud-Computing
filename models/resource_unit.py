from models.resource_type import ResourceType


class ResourceUnit:
    def __init__(
        self, resourceType: ResourceType, execution_time: float, execution_cost: float
    ):
        self.resourceType = resourceType
        self.execution_time = execution_time
        self.execution_cost = execution_cost

    def __repr__(self) -> str:
        return f"Resource Type: {self.resourceType}, ET: {self.execution_time}, EC: {self.execution_cost}"
