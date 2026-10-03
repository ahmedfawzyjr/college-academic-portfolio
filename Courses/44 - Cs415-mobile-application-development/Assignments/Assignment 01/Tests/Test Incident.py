import os

def test_dart_file():
    test_dir = os.path.dirname(os.path.abspath(__file__))
    dart_path = os.path.join(test_dir, '..', 'solution', 'incident.dart')
    assert os.path.exists(dart_path), f'Missing Dart file at {dart_path}'
    print('Mobile Dev Assignment 01 Test Passed!')

if __name__ == '__main__':
    test_dart_file()
