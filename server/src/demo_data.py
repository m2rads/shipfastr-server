import distance_matrix 


def create_data():
  """Creates the data."""
  data = {}
  # data['API_key'] = 'AIzaSyAljGQx6PV8wK63qHQXjl5FJ3UZDeXta2Y'
  data['addresses'] = ['3610+Hacks+Cross+Rd+Memphis+TN', # depot
                       '1921+Elvis+Presley+Blvd+Memphis+TN',
                       '149+Union+Avenue+Memphis+TN',
                       '1034+Audubon+Drive+Memphis+TN',
                       '1532+Madison+Ave+Memphis+TN',
                       '706+Union+Ave+Memphis+TN',
                       '3641+Central+Ave+Memphis+TN',
                       '926+E+McLemore+Ave+Memphis+TN',
                       '4339+Park+Ave+Memphis+TN',
                       '600+Goodwyn+St+Memphis+TN',
                       '2000+North+Pkwy+Memphis+TN',
                       '262+Danny+Thomas+Pl+Memphis+TN',
                       '125+N+Front+St+Memphis+TN',
                       '5959+Park+Ave+Memphis+TN',
                       '814+Scott+St+Memphis+TN',
                       '1005+Tillman+St+Memphis+TN'
                      ]
  return data


def create_demo_distance_matrix(): 
    data = create_data()
    data['API_key'] = 'AIzaSyAljGQx6PV8wK63qHQXjl5FJ3UZDeXta2Y'
    matrices = distance_matrix.create_distance_matrix(data)
    distance_matrix_data = {}
    distance_matrix_data["distance_matrix"] = matrices
    distance_matrix_data["num_vehicles"] = 5
    distance_matrix_data['depot'] = 0
    return distance_matrix_data