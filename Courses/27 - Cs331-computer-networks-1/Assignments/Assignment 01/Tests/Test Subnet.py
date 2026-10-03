import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution')))
from subnet_calculator import calculate_subnet

def test_subnet():
    info = calculate_subnet('192.168.1.0/24')
    assert info['network_address'] == '192.168.1.0'
    assert info['broadcast_address'] == '192.168.1.255'
    assert info['num_hosts'] == 254
    print('Networks Assignment 01 Test Passed!')

if __name__ == '__main__':
    test_subnet()
