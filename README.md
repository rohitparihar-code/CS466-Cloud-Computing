# QoS aware FaaS for Heterogeneous Edge-Cloud continuum

The research paper 'QoS aware FaaS for Heterogeneous Edge-Cloud continuum' discusses about a heterogeneous FaaS platform that deduces function resource specification using Machine Learning (ML) methods, performs smart function placement on Edge/Cloud based on a user-specified QoS requirement.

We have attempted to create a similar functional program in this repository.

## Getting Started

To use this software, you will need to install Python 3 and the required dependencies listed in requirements.txt and finally run the main.py file to see the program run.

- Ensure you have python version 3+ installed

1. Clone this repository: `git clone https://github.com/rohitparihar-code/cc-implementation.git`
2. `cd cc-implementation`
3. Run `pip install -r requirements.txt` to install the required dependencies
4. Run `python3 main.py` to run the program

## Project Structure

The code is organized into several Python modules:

- utils.py: This file contains utility functions used by other functions, such as `get_execution_time`, `applyQosFilter`, and `execute_function`.

- example_functions/functions.py: This file contains sample functions to be executed.

- models/resource_type.py: Defines the ResourceType class, which represents a type of resource (e.g. an edge device or cloud instance).

- models/qos.py: Defines the Qos class, which represents the Quality of Service requirements for a function.

- models/resource_unit.py: Defines the ResourceUnit class, which represents a unit of a resource (i.e. an instance of a ResourceType) with the expected execution time and cost for a function.

- main.py: Contains the primary functions such as `frontend_server`, `faas_resource_manager`, `analytics_engine` and `function_deployment`.

## Function Description

### predict_execution_time(fn, \*params) -> list[ResourceUnit]

This function takes a function and its parameters as input and returns a list of ResourceUnit objects representing the probable resources that can be used to execute the function. The predict_execution_time function uses a base resource to estimate the execution time for the function on different resource types. The estimated execution time and cost for each resource type are stored in a ResourceUnit object and added to the list that is returned.

### estimate_hr_exec_time(et_fi_base: float) -> list[ResourceUnit]

This function takes a reference execution time as input and returns a list of ResourceUnit objects representing the estimated execution time and cost for the function on different resource types. The estimate_hr_exec_time function calculates the estimated execution time and cost for each resource type using the et_mul and ec_mul properties of the ResourceType object.

### function_deployment(candidate_list: list[ResourceUnit])

This function takes a list of ResourceUnit objects representing candidate resources that can execute a function and deploys the function to the first compatible resource in the list. If no compatible resource is found, None is returned.

### analytics_engine(function_name, function_params)

This function takes a function name and its parameters as input and returns a list of ResourceUnit objects representing the probable resources that can be used to execute the function. The analytics_engine function selects the appropriate ML model for the function and uses it to predict the execution time on different resource types.

### faas_resource_manager(function_input, user_qos: Qos)

This function takes a function input and a Qos object representing the user's quality of service requirements as input and returns a list of ResourceUnit objects representing the probable resources

# Additional Resource

1. [QoS aware FaaS for Heterogeneous Edge-Cloud continuum](https://ieeexplore.ieee.org/abstract/document/9860835)

# License

This project uses the GNU General Public License v3.0.
