class ResourceType:
    def __init__(
        self,
        name: str,
        et_mul: float,
        ec_mul: float,
        instances_avail: int,
        instances_deployed: int,
    ):
        self.name = name
        self.et_mul = et_mul
        self.ec_mul = ec_mul
        self.instances_deployed = instances_deployed
        self.instances_avail = instances_avail

    def remove_worker_instance(self):
        self.instances_deployed -= 1

    def add_worker_instance(self):
        self.instances_deployed += 1

    def check_worker_for_compatibility(self) -> bool:
        return (self.instances_avail - self.instances_deployed) > 1

    def __repr__(self) -> str:
        return f"Resource Name: {self.name}"
