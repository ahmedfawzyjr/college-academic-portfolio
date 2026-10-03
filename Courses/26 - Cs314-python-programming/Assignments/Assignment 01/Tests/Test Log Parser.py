import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'solution')))
from log_parser import parse_logs

def test_parse_logs():
    logs = ['GET / 200', 'GET / 200', 'GET /fail 404']
    res = parse_logs(logs)
    assert res['200'] == 2
    assert res['404'] == 1
    print('Python Assignment 01 Test Passed!')

if __name__ == '__main__':
    test_parse_logs()
