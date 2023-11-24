import argparse

class Parameters:
    """Global parameters"""
    def __init__(self, **kwargs):
        self.param1 = kwargs.get('param1', 'default_value1')
        self.param2 = kwargs.get('param2', 'default_value2')

def view_parameters(input_parameters):
    print("Parameters:")
    print("param1: {}".format(input_parameters.param1))
    print("param2: {}".format(input_parameters.param2))

parser = argparse.ArgumentParser(description='Testing parameters')
parser.add_argument('-p1', '--param1', help='Parameter 1')
parser.add_argument('-p2', '--param2', help='Parameter 2')
params = parser.parse_args()
input_parameters = Parameters(param1=params.param1, param2=params.param2)
view_parameters(input_parameters)
