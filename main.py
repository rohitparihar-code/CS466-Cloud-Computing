from utils import *
from example_functions.functions import *
from models.resource_type import *
from models.qos import Qos
from models.resource_unit import ResourceUnit

RESOURCE_SET = {
    ResourceType("edge_1", 1.0, 1.0, 6, 0),
    ResourceType("edge_2", 0.85, 1.5, 4, 0),
    ResourceType("cloud_1", 0.5, 3.0, 2, 0),
    ResourceType("cloud_2", 0.35, 5.0, 2, 0),
}


def predict_execution_time(fn, *params) -> list[ResourceUnit]:
    # Takes function and its parameters as input (function: fi, parameters: p1, p2, p3, ... pn)
    # returns the probable list of resources that can be used with their estimated execution time and cost

    # returns the expected execution time for a function on base resource
    et_fi_base = get_execution_time(fn, *params)

    # Estimate execution time for different resource types
    probable_list = estimate_hr_exec_time(et_fi_base)
    return probable_list


def estimate_hr_exec_time(et_fi_base: float) -> list[ResourceUnit]:
    # Returns a list of estimated execution costs and time for heterogenous resources for a function based on a reference execution time

    probable_list = []

    # Time-cost Estimation Phase for different resource types
    for rj in RESOURCE_SET:
        # et_fi_rj = psi(fi, rj, srj) * et_fi_base
        et_fi_rj = rj.et_mul * et_fi_base
        # ec_fi_rj = omega(rj, srj) * et_fi_rj
        ec_fi_rj = rj.ec_mul * et_fi_rj
        # A tuple is formed and added to the probable
        # res_unit = (rj, srj, et_fi_rj, ec_fi_rj)
        res_unit = ResourceUnit(rj, et_fi_rj, ec_fi_rj)
        probable_list.append(res_unit)

    return probable_list


def function_deployment(candidate_list: list[ResourceUnit]):
    """
    Takes a candidate list as input and returns a worker that satisfies the QoS metric and has available
    resources to service the function execution request.

    :param candidate_list: A list of candidate workers that can service the function execution request which satisfies the QOS metric.
    :return: The worker that satisfies the QoS metric and has available resources to service the function execution request.
    """

    for res_unit in candidate_list:
        res_type = res_unit.resourceType
        if res_type.check_worker_for_compatibility():
            res_type.add_worker_instance()
        # Dispatching the function execution
        # 11: cw.execute_function(fi, param_location, res_spec)
        break

    return None


def analytics_engine(function_name, function_params):
    # Takkes function and its parameters as input and returns the probable list of resources configs that can be used

    # Model selection and prediction
    # Identifies the appropriate ML model (one model for each function) and returns the appropriate resource configurations
    # based on the execution time

    return predict_execution_time(function_name, function_params)


def faas_resource_manager(function_input, user_qos: Qos):
    # Extract the event name and input data from the function input
    event_name = function_input.get("event_name")
    input_data = function_input.get("input_data")

    (function_name, qos_specs) = event_database(event_name=event_name)

    resource_list = analytics_engine(function_name, input_data)

    filtered_hr_list = applyQosFilter(resource_list, user_qos)

    # Return the function name and QoS specifications as a tuple
    return filtered_hr_list


def frontend_server(request):
    # Extract the event name, function-assisted input, and payload from the request
    event_name = request.GET.get("event_name")
    function_input = request.GET.get("function_input")
    payload = request.GET.get("payload")

    # Perform any necessary processing based on the event name and input data
    if faas_resource_manager == "get_specifications":
        result = faas_resource_manager(function_input, payload)
        result1 = analytics_engine(result[0], result[1])

    elif event_name == "send_email":
        result = send_email(function_input, payload)
    else:
        result = {"error": "Invalid event name"}

    # Return the result as a JSON response
    return JsonResponse(result)
