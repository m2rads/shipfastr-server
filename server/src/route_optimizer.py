"""Simple Vehicles Routing Problem (VRP).

   This is a sample using the routing library python wrapper to solve a VRP
   problem.
   A description of the problem can be found here:
   http://en.wikipedia.org/wiki/Vehicle_routing_problem.

   Distances are in meters.
"""

from dis import dis
from turtle import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

import distance_matrix 


def create_demo_distance_matrix(): 
    data = distance_matrix.create_data()
    data['API_key'] = 'AIzaSyAljGQx6PV8wK63qHQXjl5FJ3UZDeXta2Y'
    matrices = distance_matrix.create_distance_matrix(data)
    distance_matrix_data = {}
    distance_matrix_data["distance_matrix"] = matrices
    distance_matrix_data["num_vehicles"] = 5
    distance_matrix_data['depot'] = 0
    return distance_matrix_data


def print_solution(data, manager, routing, solution):
    """Prints solution on console."""
    print(f'Objective: {solution.ObjectiveValue()}')
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
        index = routing.Start(vehicle_id)
        plan_output = 'Route for vehicle {}:\n'.format(vehicle_id)
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += ' {} -> '.format(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(
                previous_index, index, vehicle_id)
        plan_output += '{}\n'.format(manager.IndexToNode(index))
        plan_output += 'Distance of the route: {}m\n'.format(route_distance)
        print(plan_output)
        max_route_distance = max(route_distance, max_route_distance)
    print('Maximum of the route distances: {}m'.format(max_route_distance))

def create_response(data, manager, routing, solution):
    reponse_data = {}
    max_route_distance = 0
    for vehicle_id in range(data['num_vehicles']):
            index = routing.Start(vehicle_id)
            reponse_data[f'{vehicle_id}'] = []
            route_distance = 0
            while not routing.IsEnd(index):
                reponse_data[f'{vehicle_id}'].append(manager.IndexToNode(index))
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(
                    previous_index, index, vehicle_id)
            reponse_data[f'{vehicle_id}'].append(manager.IndexToNode(index))
            max_route_distance = max(route_distance, max_route_distance)
    return reponse_data



def optimizer(source):
    """Entry point of the program."""
    # Instantiate the data problem.
    # data = create_data_model()
    # data = create_demo_distance_matrix()
    data = source

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)


    # Create and register a transit callback.
    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add Distance constraint.
    dimension_name = 'Distance'
    routing.AddDimension(
        transit_callback_index,
        2,  # no slack
        100000,  # vehicle maximum travel distance
        True,  # start cumul to zero
        dimension_name)
    distance_dimension = routing.GetDimensionOrDie(dimension_name)
    distance_dimension.SetGlobalSpanCostCoefficient(100)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution on console.
    if solution:
        # print_solution(data, manager, routing, solution)
        return create_response(data, manager, routing, solution)
    else:
        # print('No solution found !')
        return "no solution found!"


# if __name__ == '__main__':
#     main()