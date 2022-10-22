"""Simple Vehicles Routing Problem (VRP).

   This is a sample using the routing library python wrapper to solve a VRP
   problem.
   A description of the problem can be found here:
   http://en.wikipedia.org/wiki/Vehicle_routing_problem.

   Distances are in meters.

   Source for this code: 
   https://developers.google.com/optimization/routing/vrp.
"""

from dis import dis
from turtle import distance
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp




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

    # return solution.
    if solution:
        return create_response(data, manager, routing, solution)
    else:
        return "no solution found!"

